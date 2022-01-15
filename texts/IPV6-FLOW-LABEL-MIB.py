#
# PySNMP MIB module IPV6-FLOW-LABEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-FLOW-LABEL-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, iso, Integer32, mib_2, Bits, Counter32, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "iso", "Integer32", "mib-2", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipv6FlowLabelMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 103))
ipv6FlowLabelMIB.setRevisions(('2003-08-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipv6FlowLabelMIB.setRevisionsDescriptions(('Initial version, published as RFC 3595.',))
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setLastUpdated('200308280000Z')
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setOrganization('IETF Operations and Management Area')
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setContactInfo('Bert Wijnen (Editor) \n                      Lucent Technologies \n                      Schagen 33 \n                      3461 GL Linschoten \n                      Netherlands \n                      Phone: +31 348-407-775 \n                      EMail: bwijnen@lucent.com \n \n                      Send comments to <mibs@ops.ietf.org>. \n                     ')
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setDescription('This MIB module provides commonly used textual \n                      conventions for IPv6 Flow Labels. \n \n                      Copyright (C) The Internet Society (2003).  This \n                      version of this MIB module is part of RFC 3595, \n                      see the RFC itself for full legal notices. \n                     ')
class IPv6FlowLabel(TextualConvention, Integer32):
    reference = 'Internet Protocol, Version 6 (IPv6) specification, \n                      section 6.  RFC 2460. \n                     '
    description = 'The flow identifier or Flow Label in an IPv6 \n                      packet header that may be used to discriminate \n                      traffic flows. \n                     '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1048575)

class IPv6FlowLabelOrAny(TextualConvention, Integer32):
    description = 'The flow identifier or Flow Label in an IPv6 \n                      packet header that may be used to discriminate \n                      traffic flows.  The value of -1 is used to \n                      indicate a wildcard, i.e. any value. \n                     '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048575), )
mibBuilder.exportSymbols("IPV6-FLOW-LABEL-MIB", IPv6FlowLabelOrAny=IPv6FlowLabelOrAny, ipv6FlowLabelMIB=ipv6FlowLabelMIB, IPv6FlowLabel=IPv6FlowLabel, PYSNMP_MODULE_ID=ipv6FlowLabelMIB)
