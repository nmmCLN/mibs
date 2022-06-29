#
# PySNMP MIB module ATM-DXI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/atmforum/ATM-DXI-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:03 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ObjectIdentity, MibIdentifier, Integer32, Bits, Unsigned32, iso, Gauge32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ObjectIdentity", "MibIdentifier", "Integer32", "Bits", "Unsigned32", "iso", "Gauge32", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmUniDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 3))
class Dfa(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16777215)

atmDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 3, 2))
atmDxiConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 3, 2, 2), )
if mibBuilder.loadTexts: atmDxiConfTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfTable.setDescription('This table contains\n\tATM DXI configuration information\n\tincluding information on the mode supported\n\tacross the DXI.')
atmDxiConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1), ).setIndexNames((0, "ATM-DXI-MIB", "atmDxiConfIfIndex"))
if mibBuilder.loadTexts: atmDxiConfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfEntry.setDescription('This list contains ATM DXI configuration information.')
atmDxiConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiConfIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfIfIndex.setDescription('The value of this object identifies, for SNMP, the ATM DXI\n\tinterface for which this entry contains management information.\n\tThis is the same value as used to identify the IfEntry describing\n\tthe DCE interface.  Management uses and expects this value.  In\n\tthe proxy mode of operation, the DCE always treats this as 0, but\n\tpreserves it in its response to the DTE.  0, the DXI value, means\n\tthe interface over which the DXI LMI request was received.')
atmDxiConfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mode1a", 1), ("mode1b", 2), ("mode2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDxiConfMode.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiConfMode.setDescription('This object identifies the dxi mode being\n\tused at the atm dxi port.')
atmDxiDFAConfTable = MibTable((1, 3, 6, 1, 4, 1, 353, 3, 2, 3), )
if mibBuilder.loadTexts: atmDxiDFAConfTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfTable.setDescription('This table contains configuration information about\n\ta particular DFA.')
atmDxiDFAConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1), ).setIndexNames((0, "ATM-DXI-MIB", "atmDxiDFAConfIfIndex"), (0, "ATM-DXI-MIB", "atmDxiDFAConfDfaIndex"))
if mibBuilder.loadTexts: atmDxiDFAConfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfEntry.setDescription('This list contains ATM DXI DFA configuration\n\tinformation.')
atmDxiDFAConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiDFAConfIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfIfIndex.setDescription('The value of this object identifies, for SNMP, the ATM DXI\n\tinterface for which this entry contains management information.\n\tThis is the same value as used to identify the IfEntry describing\n\tthe DCE interface.  Management uses and expects this value.  In\n\tthe proxy mode of operation, the DCE always treats this as 0, but\n\tpreserves it in its response to the DTE.  0, the DXI value, means\n\tthe interface over which the DXI LMI request was received.')
atmDxiDFAConfDfaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 2), Dfa()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDxiDFAConfDfaIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfDfaIndex.setDescription('This object identifies the DFA instance on the DXI\n\tidentified by atmDxiDFAConfIfIndex.')
atmDxiDFAConfAALType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("none", 2), ("aal34", 3), ("aal5", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDxiDFAConfAALType.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiDFAConfAALType.setDescription('This object identifies the AAL type supported at this DFA.\n\tNote, if mode 2 is supported on the DXI identified by the\n\tcorresponding instance of atmDxiDFAConfIfIndex and that\n\tinstance of atmDxiDFAConfIfIndex identifies the DCE side\n\tof the DXI, then this object contains the AAL Type being\n\trun on the corresponding VPI/VCI on the corresponding ATM UNI\n\tinterface.')
atmDxiEnterprise = MibScalar((1, 3, 6, 1, 4, 1, 353, 3, 2, 4), ObjectIdentifier())
if mibBuilder.loadTexts: atmDxiEnterprise.setStatus('mandatory')
if mibBuilder.loadTexts: atmDxiEnterprise.setDescription("This object is included as the first ID-Value pair\n\tin a Trap PDU for which the Generic Trap Type field\n\thas the value 'enterpriseSpecific'.  The value of the\n\tobject identifies the enterprise under whose authority\n\tthe value of the Enterprise Trap Type field is defined.")
mibBuilder.exportSymbols("ATM-DXI-MIB", Dfa=Dfa, atmDxiConfEntry=atmDxiConfEntry, atmDxiEnterprise=atmDxiEnterprise, atmDxiConfTable=atmDxiConfTable, atmDxiDFAConfEntry=atmDxiDFAConfEntry, atmDxiDFAConfAALType=atmDxiDFAConfAALType, atmForum=atmForum, atmDxiConfIfIndex=atmDxiConfIfIndex, atmUniDxi=atmUniDxi, atmDxi=atmDxi, atmDxiDFAConfDfaIndex=atmDxiDFAConfDfaIndex, atmDxiDFAConfTable=atmDxiDFAConfTable, atmDxiDFAConfIfIndex=atmDxiDFAConfIfIndex, atmDxiConfMode=atmDxiConfMode)
