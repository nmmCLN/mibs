#
# PySNMP MIB module SNMP-PROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-PROXY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:47 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
SnmpEngineID, SnmpAdminString = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpEngineID", "SnmpAdminString")
SnmpTagValue, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "SnmpTagValue")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, snmpModules, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "snmpModules", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, RowStatus, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "StorageType")
snmpProxyMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 14))
snmpProxyMIB.setRevisions(('2002-10-14 00:00', '1998-08-04 00:00', '1997-07-14 00:00',))
if mibBuilder.loadTexts: snmpProxyMIB.setLastUpdated('200210140000Z')
if mibBuilder.loadTexts: snmpProxyMIB.setOrganization('IETF SNMPv3 Working Group')
snmpProxyObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 1))
snmpProxyConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3))
snmpProxyTable = MibTable((1, 3, 6, 1, 6, 3, 14, 1, 2), )
if mibBuilder.loadTexts: snmpProxyTable.setStatus('current')
snmpProxyEntry = MibTableRow((1, 3, 6, 1, 6, 3, 14, 1, 2, 1), ).setIndexNames((1, "SNMP-PROXY-MIB", "snmpProxyName"))
if mibBuilder.loadTexts: snmpProxyEntry.setStatus('current')
snmpProxyName = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: snmpProxyName.setStatus('current')
snmpProxyType = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("trap", 3), ("inform", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyType.setStatus('current')
snmpProxyContextEngineID = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 3), SnmpEngineID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyContextEngineID.setStatus('current')
snmpProxyContextName = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyContextName.setStatus('current')
snmpProxyTargetParamsIn = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyTargetParamsIn.setStatus('current')
snmpProxySingleTargetOut = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxySingleTargetOut.setStatus('current')
snmpProxyMultipleTargetOut = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 7), SnmpTagValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyMultipleTargetOut.setStatus('current')
snmpProxyStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyStorageType.setStatus('current')
snmpProxyRowStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyRowStatus.setStatus('current')
snmpProxyCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3, 1))
snmpProxyGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3, 2))
snmpProxyCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 14, 3, 1, 1)).setObjects(("SNMP-TARGET-MIB", "snmpTargetBasicGroup"), ("SNMP-TARGET-MIB", "snmpTargetResponseGroup"), ("SNMP-PROXY-MIB", "snmpProxyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpProxyCompliance = snmpProxyCompliance.setStatus('current')
snmpProxyGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 14, 3, 2, 3)).setObjects(("SNMP-PROXY-MIB", "snmpProxyType"), ("SNMP-PROXY-MIB", "snmpProxyContextEngineID"), ("SNMP-PROXY-MIB", "snmpProxyContextName"), ("SNMP-PROXY-MIB", "snmpProxyTargetParamsIn"), ("SNMP-PROXY-MIB", "snmpProxySingleTargetOut"), ("SNMP-PROXY-MIB", "snmpProxyMultipleTargetOut"), ("SNMP-PROXY-MIB", "snmpProxyStorageType"), ("SNMP-PROXY-MIB", "snmpProxyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpProxyGroup = snmpProxyGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-PROXY-MIB", PYSNMP_MODULE_ID=snmpProxyMIB, snmpProxyCompliance=snmpProxyCompliance, snmpProxyContextEngineID=snmpProxyContextEngineID, snmpProxyMIB=snmpProxyMIB, snmpProxyTable=snmpProxyTable, snmpProxySingleTargetOut=snmpProxySingleTargetOut, snmpProxyObjects=snmpProxyObjects, snmpProxyName=snmpProxyName, snmpProxyRowStatus=snmpProxyRowStatus, snmpProxyTargetParamsIn=snmpProxyTargetParamsIn, snmpProxyConformance=snmpProxyConformance, snmpProxyMultipleTargetOut=snmpProxyMultipleTargetOut, snmpProxyStorageType=snmpProxyStorageType, snmpProxyGroups=snmpProxyGroups, snmpProxyGroup=snmpProxyGroup, snmpProxyType=snmpProxyType, snmpProxyCompliances=snmpProxyCompliances, snmpProxyEntry=snmpProxyEntry, snmpProxyContextName=snmpProxyContextName)
