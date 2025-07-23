#include <core.p4>
#include <v1model.p4>

// Ethernet header
header ethernet_t {
    bit<48> dstAddr;
    bit<48> srcAddr;
    bit<16> etherType;
}

// IPv4 header
header ipv4_t {
    bit<4>  version;
    bit<4>  ihl;
    bit<8>  diffserv;
    bit<16> totalLen;
    bit<16> identification;
    bit<3>  flags;
    bit<13> fragOffset;
    bit<8>  ttl;
    bit<8>  protocol;
    bit<16> hdrChecksum;
    bit<32> srcAddr;
    bit<32> dstAddr;
}

// Metadata (empty)
struct metadata {}

// Headers
struct headers {
    ethernet_t ethernet;
    ipv4_t ipv4;
}

// Parser
parser ParserImpl(packet_in packet,
                  out headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {
    state start {
        packet.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType) {
            0x0800: parse_ipv4;
            default: accept;
        }
    }
    state parse_ipv4 {
        packet.extract(hdr.ipv4);
        transition accept;
    }
}

// Registers
register<bit<64>>(5) statusReg; 
// 0: pkt_counter
// 1: alarm
// 2: Hnorm
// 3: ewma
// 4: threshold

control ingress(inout headers hdr,
                inout metadata meta,
                inout standard_metadata_t standard_metadata) {

    action ipv4_forward(bit<48> dstMac, bit<9> port) {
        hdr.ethernet.dstAddr = dstMac;
        standard_metadata.egress_spec = port;
    }

    action _drop() {
        mark_to_drop();
    }

    table ipv4_lpm {
        key = {
            hdr.ipv4.dstAddr: lpm;
        }
        actions = {
            ipv4_forward;
            _drop;
        }
        size = 1024;
    }

apply {
    bit<64> pkt_counter;
    bit<1> alarm;
    bit<64> Hnorm;
    bit<64> ewma;
    bit<64> threshold;

    // Đọc giá trị trước đó
    statusReg.read(pkt_counter, 0);
    statusReg.read(Hnorm, 2);
    statusReg.read(ewma, 3);
    statusReg.read(threshold, 4);

    if (hdr.ipv4.isValid() && hdr.ipv4.dstAddr == 0x0A000101) {
        // Gói tin đến victim -> tăng counter
        pkt_counter = pkt_counter + 1;

        // Hnorm giảm dần theo số packet
        if (pkt_counter >= 500) {
            Hnorm = 512;
        } else if (pkt_counter >= 100) {
            Hnorm = 1024;
        } else {
            Hnorm = 2048;
        }

        // EWMA cập nhật từ Hnorm mới nhất
        if (ewma > 0) {
            // ewma = alpha * Hnorm + (1-alpha)*ewma
            // alpha = 0.3, nhân 1024:
            //   ewma = 307*Hnorm + 891*(ewma/1024)
            ewma = (307 * Hnorm + 891 * (ewma / 1024));
        } else {
            ewma = Hnorm;
        }

        // threshold = ewma - epsilon (epsilon=10)
        if (ewma > 10) {
            threshold = ewma - 10;
        } else {
            threshold = 0;
        }

        // So sánh để xác định alarm
        if (Hnorm < threshold) {
            alarm = 1;
        } else {
            alarm = 0;
        }
    } else {
        // Không phải gói đến victim -> reset
        pkt_counter = 0;
        Hnorm = 2048;
        ewma = 0;
        threshold = 2048;
        alarm = 0;
    }

    // Ghi lại giá trị
    statusReg.write(0, pkt_counter);
    statusReg.write(1, (bit<64>)alarm);
    statusReg.write(2, Hnorm);
    statusReg.write(3, ewma);
    statusReg.write(4, threshold);

    ipv4_lpm.apply();
}
}

// Egress trống
control egress(inout headers hdr,
               inout metadata meta,
               inout standard_metadata_t standard_metadata) {
    apply { }
}

// Không checksum
control verifyChecksum(inout headers hdr, inout metadata meta) { apply {} }
control computeChecksum(inout headers hdr, inout metadata meta) { apply {} }

// Deparser
control DeparserImpl(packet_out packet, in headers hdr) {
    apply {
        packet.emit(hdr.ethernet);
        packet.emit(hdr.ipv4);
    }
}

// Main pipeline
V1Switch(ParserImpl(),
         verifyChecksum(),
         ingress(),
         egress(),
         computeChecksum(),
         DeparserImpl()) main;
