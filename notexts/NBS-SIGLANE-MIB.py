#
# PySNMP MIB module NBS-SIGLANE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-SIGLANE-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:24:41 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NbsCmmcChannelBand, = mibBuilder.importSymbols("NBS-CMMCENUM-MIB", "NbsCmmcChannelBand")
nbs, NbsTcMHz, NbsTcTemperature, NbsTcMicroAmp, NbsTcMilliDb = mibBuilder.importSymbols("NBS-MIB", "nbs", "NbsTcMHz", "NbsTcTemperature", "NbsTcMicroAmp", "NbsTcMilliDb")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, ModuleIdentity, Gauge32, Unsigned32, TimeTicks, Bits, Integer32, ObjectIdentity, MibIdentifier, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "ModuleIdentity", "Gauge32", "Unsigned32", "TimeTicks", "Bits", "Integer32", "ObjectIdentity", "MibIdentifier", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsSigLaneMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 236))
if mibBuilder.loadTexts: nbsSigLaneMib.setLastUpdated('201710180000Z')
if mibBuilder.loadTexts: nbsSigLaneMib.setOrganization('NBS')
nbsSigLanePortGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 236, 10))
if mibBuilder.loadTexts: nbsSigLanePortGrp.setStatus('current')
nbsSigLaneLaneGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 236, 20))
if mibBuilder.loadTexts: nbsSigLaneLaneGrp.setStatus('current')
nbsSigLaneTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 236, 100))
if mibBuilder.loadTexts: nbsSigLaneTraps.setStatus('current')
nbsSigLaneTraps0 = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 236, 100, 0))
if mibBuilder.loadTexts: nbsSigLaneTraps0.setStatus('current')
nbsSigLanePortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 236, 10, 1), )
if mibBuilder.loadTexts: nbsSigLanePortTable.setStatus('current')
nbsSigLanePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1), ).setIndexNames((0, "NBS-SIGLANE-MIB", "nbsSigLanePortIfIndex"))
if mibBuilder.loadTexts: nbsSigLanePortEntry.setStatus('current')
nbsSigLanePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLanePortIfIndex.setStatus('current')
nbsSigLanePortFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("fiber", 2), ("lambda", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLanePortFacility.setStatus('current')
nbsSigLanePortLanes = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLanePortLanes.setStatus('current')
nbsSigLaneLaneTable = MibTable((1, 3, 6, 1, 4, 1, 629, 236, 20, 1), )
if mibBuilder.loadTexts: nbsSigLaneLaneTable.setStatus('current')
nbsSigLaneLaneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1), ).setIndexNames((0, "NBS-SIGLANE-MIB", "nbsSigLaneLaneIfIndex"), (0, "NBS-SIGLANE-MIB", "nbsSigLaneLaneIndex"))
if mibBuilder.loadTexts: nbsSigLaneLaneEntry.setStatus('current')
nbsSigLaneLaneIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneIfIndex.setStatus('current')
nbsSigLaneLaneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneIndex.setStatus('current')
nbsSigLaneLaneFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 10), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneFrequency.setStatus('current')
nbsSigLaneLaneWavelengthX = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneWavelengthX.setStatus('current')
nbsSigLaneLaneChannelBand = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 12), NbsCmmcChannelBand()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneChannelBand.setStatus('current')
nbsSigLaneLaneChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneChannelNumber.setStatus('current')
nbsSigLaneLaneTxDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("no", 2), ("yes", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigLaneLaneTxDisable.setStatus('current')
nbsSigLaneLaneFaultsCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneFaultsCaps.setStatus('current')
nbsSigLaneLaneFaultsOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneFaultsOper.setStatus('current')
nbsSigLaneLaneTxPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 1), ("lowAlarm", 2), ("lowWarning", 3), ("ok", 4), ("highWarning", 5), ("highAlarm", 6))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneTxPowerLevel.setStatus('current')
nbsSigLaneLaneTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 21), NbsTcMilliDb().clone(-2147483648)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneTxPower.setStatus('current')
nbsSigLaneLaneTxPowerAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 22), NbsTcMilliDb().clone(-2147483648)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigLaneLaneTxPowerAdmin.setStatus('current')
nbsSigLaneLaneRxPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 1), ("lowAlarm", 2), ("lowWarning", 3), ("ok", 4), ("highWarning", 5), ("highAlarm", 6))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneRxPowerLevel.setStatus('current')
nbsSigLaneLaneRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 31), NbsTcMilliDb().clone(-2147483648)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneRxPower.setStatus('current')
nbsSigLaneLaneBiasAmpsLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 1), ("lowAlarm", 2), ("lowWarning", 3), ("ok", 4), ("highWarning", 5), ("highAlarm", 6))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneBiasAmpsLevel.setStatus('current')
nbsSigLaneLaneBiasAmps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 41), NbsTcMicroAmp().clone(-1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneBiasAmps.setStatus('current')
nbsSigLaneLaneLaserTempLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notSupported", 1), ("lowAlarm", 2), ("lowWarning", 3), ("ok", 4), ("highWarning", 5), ("highAlarm", 6))).clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneLaserTempLevel.setStatus('current')
nbsSigLaneLaneLaserTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 51), NbsTcTemperature().clone(-2147483648)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneLaserTemp.setStatus('current')
nbsSigLaneLaneEthTxAllOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 60), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneEthTxAllOctets.setStatus('current')
nbsSigLaneLaneEthTxAllFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 61), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneEthTxAllFrames.setStatus('current')
nbsSigLaneLaneEthRxAllOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 70), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneEthRxAllOctets.setStatus('current')
nbsSigLaneLaneEthRxAllFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 71), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigLaneLaneEthRxAllFrames.setStatus('current')
mibBuilder.exportSymbols("NBS-SIGLANE-MIB", PYSNMP_MODULE_ID=nbsSigLaneMib, nbsSigLanePortLanes=nbsSigLanePortLanes, nbsSigLaneLaneRxPower=nbsSigLaneLaneRxPower, nbsSigLaneTraps=nbsSigLaneTraps, nbsSigLaneLaneEthTxAllFrames=nbsSigLaneLaneEthTxAllFrames, nbsSigLaneLaneChannelBand=nbsSigLaneLaneChannelBand, nbsSigLaneLaneFaultsCaps=nbsSigLaneLaneFaultsCaps, nbsSigLanePortGrp=nbsSigLanePortGrp, nbsSigLaneLaneIndex=nbsSigLaneLaneIndex, nbsSigLanePortFacility=nbsSigLanePortFacility, nbsSigLaneLaneEthRxAllFrames=nbsSigLaneLaneEthRxAllFrames, nbsSigLanePortIfIndex=nbsSigLanePortIfIndex, nbsSigLaneLaneGrp=nbsSigLaneLaneGrp, nbsSigLaneTraps0=nbsSigLaneTraps0, nbsSigLaneLaneWavelengthX=nbsSigLaneLaneWavelengthX, nbsSigLaneLaneChannelNumber=nbsSigLaneLaneChannelNumber, nbsSigLaneLaneTxPowerAdmin=nbsSigLaneLaneTxPowerAdmin, nbsSigLaneLaneEthTxAllOctets=nbsSigLaneLaneEthTxAllOctets, nbsSigLaneLaneLaserTemp=nbsSigLaneLaneLaserTemp, nbsSigLaneLaneEntry=nbsSigLaneLaneEntry, nbsSigLaneLaneFaultsOper=nbsSigLaneLaneFaultsOper, nbsSigLaneLaneTable=nbsSigLaneLaneTable, nbsSigLaneLaneFrequency=nbsSigLaneLaneFrequency, nbsSigLaneLaneRxPowerLevel=nbsSigLaneLaneRxPowerLevel, nbsSigLanePortTable=nbsSigLanePortTable, nbsSigLaneLaneBiasAmpsLevel=nbsSigLaneLaneBiasAmpsLevel, nbsSigLaneLaneIfIndex=nbsSigLaneLaneIfIndex, nbsSigLaneLaneTxPowerLevel=nbsSigLaneLaneTxPowerLevel, nbsSigLaneLaneLaserTempLevel=nbsSigLaneLaneLaserTempLevel, nbsSigLaneLaneEthRxAllOctets=nbsSigLaneLaneEthRxAllOctets, nbsSigLaneLaneTxPower=nbsSigLaneLaneTxPower, nbsSigLanePortEntry=nbsSigLanePortEntry, nbsSigLaneMib=nbsSigLaneMib, nbsSigLaneLaneBiasAmps=nbsSigLaneLaneBiasAmps, nbsSigLaneLaneTxDisable=nbsSigLaneLaneTxDisable)
