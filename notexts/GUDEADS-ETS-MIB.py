#
# PySNMP MIB module GUDEADS-ETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gude/GUDEADS-ETS-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:08:58 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ObjectIdentity, MibIdentifier, Integer32, iso, Unsigned32, NotificationType, Counter64, TimeTicks, ModuleIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ObjectIdentity", "MibIdentifier", "Integer32", "iso", "Unsigned32", "NotificationType", "Counter64", "TimeTicks", "ModuleIdentity", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gudeads = ModuleIdentity((1, 3, 6, 1, 4, 1, 28507))
gudeads.setRevisions(('2007-05-23 12:44',))
if mibBuilder.loadTexts: gudeads.setLastUpdated('200705231244Z')
if mibBuilder.loadTexts: gudeads.setOrganization('Gude Analog- und Digitalsysteme GmbH')
etsPrimaryPowerChangeEvt = NotificationType((1, 3, 6, 1, 4, 1, 28507, 4, 0, 1)).setObjects(("GUDEADS-ETS-MIB", "etsPrimPowAvail"))
if mibBuilder.loadTexts: etsPrimaryPowerChangeEvt.setStatus('current')
etsSecondaryPowerChangeEvt = NotificationType((1, 3, 6, 1, 4, 1, 28507, 4, 0, 2)).setObjects(("GUDEADS-ETS-MIB", "etsSecPowAvail"))
if mibBuilder.loadTexts: etsSecondaryPowerChangeEvt.setStatus('current')
etsSNMPaccess = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 4, 1, 1))
etsTrapCtrl = MibScalar((1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsTrapCtrl.setStatus('current')
etsTrapIPTable = MibTable((1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 2), )
if mibBuilder.loadTexts: etsTrapIPTable.setStatus('current')
etsTrapIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 2, 1), ).setIndexNames((0, "GUDEADS-ETS-MIB", "etsTrapIPIndex"))
if mibBuilder.loadTexts: etsTrapIPEntry.setStatus('current')
etsTrapIPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: etsTrapIPIndex.setStatus('current')
etsTrapIPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024)).clone(162)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsTrapIPPort.setStatus('current')
etsTrapIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 4, 1, 1, 2, 1, 2), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsTrapIPAddr.setStatus('current')
gadsETS = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 4))
etsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 4, 1))
etsPrimPowAvail = MibScalar((1, 3, 6, 1, 4, 1, 28507, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsPrimPowAvail.setStatus('current')
etsSecPowAvail = MibScalar((1, 3, 6, 1, 4, 1, 28507, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsSecPowAvail.setStatus('current')
etsSecManualSelect = MibScalar((1, 3, 6, 1, 4, 1, 28507, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsSecManualSelect.setStatus('current')
etsEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 4, 0))
etsPowerSelect = MibScalar((1, 3, 6, 1, 4, 1, 28507, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsPowerSelect.setStatus('current')
etsConf = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 4, 3))
etsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 4, 3, 1))
etsCompls = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 4, 3, 2))
etsManualSelectEvt = NotificationType((1, 3, 6, 1, 4, 1, 28507, 4, 0, 3)).setObjects(("GUDEADS-ETS-MIB", "etsSecManualSelect"))
if mibBuilder.loadTexts: etsManualSelectEvt.setStatus('current')
etsPowerSelectEvt = NotificationType((1, 3, 6, 1, 4, 1, 28507, 4, 0, 4)).setObjects(("GUDEADS-ETS-MIB", "etsPowerSelect"))
if mibBuilder.loadTexts: etsPowerSelectEvt.setStatus('current')
etsBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28507, 4, 3, 1, 1)).setObjects(("GUDEADS-ETS-MIB", "etsPrimPowAvail"), ("GUDEADS-ETS-MIB", "etsSecPowAvail"), ("GUDEADS-ETS-MIB", "etsSecManualSelect"), ("GUDEADS-ETS-MIB", "etsPowerSelect"), ("GUDEADS-ETS-MIB", "etsTrapCtrl"), ("GUDEADS-ETS-MIB", "etsTrapIPAddr"), ("GUDEADS-ETS-MIB", "etsTrapIPPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsBasicGroup = etsBasicGroup.setStatus('current')
etsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 28507, 4, 3, 1, 2)).setObjects(("GUDEADS-ETS-MIB", "etsPrimaryPowerChangeEvt"), ("GUDEADS-ETS-MIB", "etsSecondaryPowerChangeEvt"), ("GUDEADS-ETS-MIB", "etsManualSelectEvt"), ("GUDEADS-ETS-MIB", "etsPowerSelectEvt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsNotificationGroup = etsNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("GUDEADS-ETS-MIB", etsGroups=etsGroups, etsSecManualSelect=etsSecManualSelect, etsTrapIPTable=etsTrapIPTable, etsTrapIPIndex=etsTrapIPIndex, etsConf=etsConf, etsObjects=etsObjects, etsSecondaryPowerChangeEvt=etsSecondaryPowerChangeEvt, etsBasicGroup=etsBasicGroup, etsSNMPaccess=etsSNMPaccess, etsPrimPowAvail=etsPrimPowAvail, etsEvents=etsEvents, etsPrimaryPowerChangeEvt=etsPrimaryPowerChangeEvt, etsNotificationGroup=etsNotificationGroup, etsPowerSelectEvt=etsPowerSelectEvt, etsCompls=etsCompls, etsSecPowAvail=etsSecPowAvail, gudeads=gudeads, etsPowerSelect=etsPowerSelect, etsTrapIPAddr=etsTrapIPAddr, etsManualSelectEvt=etsManualSelectEvt, etsTrapIPPort=etsTrapIPPort, etsTrapCtrl=etsTrapCtrl, etsTrapIPEntry=etsTrapIPEntry, PYSNMP_MODULE_ID=gudeads, gadsETS=gadsETS)
