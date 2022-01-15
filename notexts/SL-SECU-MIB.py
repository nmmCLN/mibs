#
# PySNMP MIB module SL-SECU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-SECU-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:44 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, ModuleIdentity, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, transmission, NotificationType, ObjectIdentity, MibIdentifier, Gauge32, Counter64, Bits, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "transmission", "NotificationType", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter64", "Bits", "iso", "IpAddress")
TextualConvention, DisplayString, TruthValue, DateAndTime, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "DateAndTime", "RowStatus")
slSecuMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24))
if mibBuilder.loadTexts: slSecuMib.setLastUpdated('201105170000Z')
if mibBuilder.loadTexts: slSecuMib.setOrganization('PacketLight Networks Ltd.')
class SlSecuType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("telnet", 1), ("ssh", 2), ("http", 3), ("https", 4), ("icmp", 5), ("snmp", 6), ("ftp", 7), ("tftp", 8), ("tl1", 9), ("tl1ssh", 10), ("wl", 11), ("snmpovertcp", 12), ("sftp", 13))

slSecuGen = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 1))
slSecuSelect = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2))
slSecuWl = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3))
slSecuEncryption = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4))
slSecuFirewallEnable = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuFirewallEnable.setStatus('current')
slSecuSelectTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1), )
if mibBuilder.loadTexts: slSecuSelectTable.setStatus('current')
slSecuSelectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1), ).setIndexNames((0, "SL-SECU-MIB", "slSecuSelectType"))
if mibBuilder.loadTexts: slSecuSelectEntry.setStatus('current')
slSecuSelectType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1, 1), SlSecuType())
if mibBuilder.loadTexts: slSecuSelectType.setStatus('current')
slSecuSelectPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuSelectPort.setStatus('current')
slSecuSelectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuSelectEnable.setStatus('current')
slSecuWlTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1), )
if mibBuilder.loadTexts: slSecuWlTable.setStatus('current')
slSecuWlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1), ).setIndexNames((0, "SL-SECU-MIB", "slSecuWlIp"))
if mibBuilder.loadTexts: slSecuWlEntry.setStatus('current')
slSecuWlIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuWlIp.setStatus('current')
slSecuWlMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuWlMask.setStatus('current')
slSecuWlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSecuWlStatus.setStatus('current')
slSecuEncryptionTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1), )
if mibBuilder.loadTexts: slSecuEncryptionTable.setStatus('current')
slSecuEncryptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1), ).setIndexNames((0, "SL-SECU-MIB", "slSecuEncryptionIfIndex"))
if mibBuilder.loadTexts: slSecuEncryptionEntry.setStatus('current')
slSecuEncryptionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuEncryptionIfIndex.setStatus('current')
slSecuEncryptionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuEncryptionEnable.setStatus('current')
slSecuEncryptionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("init", 1), ("exchange", 2), ("kdf", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuEncryptionStatus.setStatus('current')
slSecuEncryptionForceInit = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuEncryptionForceInit.setStatus('current')
slSecuEncryptionPreShared = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuEncryptionPreShared.setStatus('current')
slSecuEncryptionKeyExchangePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuEncryptionKeyExchangePeriod.setStatus('current')
slSecuEncryptionLock = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuEncryptionLock.setStatus('current')
slSecuEncryptionProtectedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("init", 1), ("exchange", 2), ("kdf", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuEncryptionProtectedStatus.setStatus('current')
mibBuilder.exportSymbols("SL-SECU-MIB", slSecuWlMask=slSecuWlMask, slSecuEncryptionIfIndex=slSecuEncryptionIfIndex, slSecuEncryptionEnable=slSecuEncryptionEnable, slSecuWlStatus=slSecuWlStatus, slSecuEncryptionLock=slSecuEncryptionLock, slSecuGen=slSecuGen, slSecuWl=slSecuWl, slSecuWlTable=slSecuWlTable, slSecuEncryptionForceInit=slSecuEncryptionForceInit, slSecuWlIp=slSecuWlIp, slSecuSelectEntry=slSecuSelectEntry, slSecuSelectTable=slSecuSelectTable, slSecuMib=slSecuMib, slSecuSelectType=slSecuSelectType, slSecuWlEntry=slSecuWlEntry, PYSNMP_MODULE_ID=slSecuMib, slSecuEncryptionEntry=slSecuEncryptionEntry, slSecuSelectPort=slSecuSelectPort, slSecuSelectEnable=slSecuSelectEnable, slSecuEncryptionStatus=slSecuEncryptionStatus, slSecuEncryption=slSecuEncryption, slSecuEncryptionPreShared=slSecuEncryptionPreShared, slSecuEncryptionProtectedStatus=slSecuEncryptionProtectedStatus, SlSecuType=SlSecuType, slSecuFirewallEnable=slSecuFirewallEnable, slSecuSelect=slSecuSelect, slSecuEncryptionTable=slSecuEncryptionTable, slSecuEncryptionKeyExchangePeriod=slSecuEncryptionKeyExchangePeriod)
