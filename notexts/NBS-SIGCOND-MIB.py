#
# PySNMP MIB module NBS-SIGCOND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-SIGCOND-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:24:41 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, ifAlias = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifAlias")
nbs, NbsTcMHz, NbsTcMilliDb = mibBuilder.importSymbols("NBS-MIB", "nbs", "NbsTcMHz", "NbsTcMilliDb")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Gauge32, Unsigned32, TimeTicks, Bits, Integer32, ObjectIdentity, NotificationType, MibIdentifier, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Gauge32", "Unsigned32", "TimeTicks", "Bits", "Integer32", "ObjectIdentity", "NotificationType", "MibIdentifier", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsSigCondMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 227))
if mibBuilder.loadTexts: nbsSigCondMib.setLastUpdated('201707270000Z')
if mibBuilder.loadTexts: nbsSigCondMib.setOrganization('NBS')
nbsSigCondVoaPortGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 227, 1))
if mibBuilder.loadTexts: nbsSigCondVoaPortGrp.setStatus('current')
nbsSigCondVoaChannelGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 227, 2))
if mibBuilder.loadTexts: nbsSigCondVoaChannelGrp.setStatus('current')
nbsSigCondRamanGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 227, 3))
if mibBuilder.loadTexts: nbsSigCondRamanGrp.setStatus('current')
nbsSigCondEqualizeGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 227, 20))
if mibBuilder.loadTexts: nbsSigCondEqualizeGrp.setStatus('current')
nbsSigCondRedundGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 227, 30))
if mibBuilder.loadTexts: nbsSigCondRedundGrp.setStatus('current')
nbsSigCondPortGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 227, 40))
if mibBuilder.loadTexts: nbsSigCondPortGrp.setStatus('current')
nbsSigCondChannelGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 227, 50))
if mibBuilder.loadTexts: nbsSigCondChannelGrp.setStatus('current')
nbsSigCondVodPortGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 227, 60))
if mibBuilder.loadTexts: nbsSigCondVodPortGrp.setStatus('current')
nbsSigCondTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 227, 200))
if mibBuilder.loadTexts: nbsSigCondTraps.setStatus('current')
nbsSigCondEvent = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 227, 200, 0))
if mibBuilder.loadTexts: nbsSigCondEvent.setStatus('current')
nbsSigCondVoaPortTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 227, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVoaPortTableSize.setStatus('current')
nbsSigCondVoaPortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 227, 1, 2), )
if mibBuilder.loadTexts: nbsSigCondVoaPortTable.setStatus('current')
nbsSigCondVoaPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1), ).setIndexNames((0, "NBS-SIGCOND-MIB", "nbsSigCondVoaPortIfIndex"))
if mibBuilder.loadTexts: nbsSigCondVoaPortEntry.setStatus('current')
nbsSigCondVoaPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsSigCondVoaPortIfIndex.setStatus('current')
nbsSigCondVoaPortRxAttenuAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondVoaPortRxAttenuAdmin.setStatus('current')
nbsSigCondVoaPortRxAttenuOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVoaPortRxAttenuOper.setStatus('current')
nbsSigCondVoaPortTxAttenuAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondVoaPortTxAttenuAdmin.setStatus('current')
nbsSigCondVoaPortTxAttenuOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVoaPortTxAttenuOper.setStatus('current')
nbsSigCondVoaChannelRangeTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 227, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVoaChannelRangeTableSize.setStatus('current')
nbsSigCondVoaChannelRangeTable = MibTable((1, 3, 6, 1, 4, 1, 629, 227, 2, 2), )
if mibBuilder.loadTexts: nbsSigCondVoaChannelRangeTable.setStatus('current')
nbsSigCondVoaChannelRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1), ).setIndexNames((0, "NBS-SIGCOND-MIB", "nbsSigCondVoaChannelRangeIfIndex"))
if mibBuilder.loadTexts: nbsSigCondVoaChannelRangeEntry.setStatus('current')
nbsSigCondVoaChannelRangeIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsSigCondVoaChannelRangeIfIndex.setStatus('current')
nbsSigCondVoaChannelRangeMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 2), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVoaChannelRangeMin.setStatus('current')
nbsSigCondVoaChannelRangeMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 3), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVoaChannelRangeMax.setStatus('current')
nbsSigCondVoaChannelRangeIncr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 4), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVoaChannelRangeIncr.setStatus('current')
nbsSigCondRamanTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 227, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondRamanTableSize.setStatus('current')
nbsSigCondRamanTable = MibTable((1, 3, 6, 1, 4, 1, 629, 227, 3, 2), )
if mibBuilder.loadTexts: nbsSigCondRamanTable.setStatus('current')
nbsSigCondRamanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1), ).setIndexNames((0, "NBS-SIGCOND-MIB", "nbsSigCondRamanIfIndex"))
if mibBuilder.loadTexts: nbsSigCondRamanEntry.setStatus('current')
nbsSigCondRamanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsSigCondRamanIfIndex.setStatus('current')
nbsSigCondRamanPumpPwrAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondRamanPumpPwrAdmin.setStatus('current')
nbsSigCondRamanPumpPwrOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondRamanPumpPwrOper.setStatus('current')
nbsSigCondEqualizeTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 227, 20, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondEqualizeTableSize.setStatus('current')
nbsSigCondEqualizeTable = MibTable((1, 3, 6, 1, 4, 1, 629, 227, 20, 2), )
if mibBuilder.loadTexts: nbsSigCondEqualizeTable.setStatus('current')
nbsSigCondEqualizeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1), ).setIndexNames((0, "NBS-SIGCOND-MIB", "nbsSigCondEqualizeIfIndex"))
if mibBuilder.loadTexts: nbsSigCondEqualizeEntry.setStatus('current')
nbsSigCondEqualizeIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondEqualizeIfIndex.setStatus('current')
nbsSigCondEqualizeState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("disabled", 2), ("enabled", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondEqualizeState.setStatus('current')
nbsSigCondEqualizeLimitMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 11), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondEqualizeLimitMin.setStatus('current')
nbsSigCondEqualizeLimitMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 12), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondEqualizeLimitMax.setStatus('current')
nbsSigCondEqualizeDesiredMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 21), NbsTcMilliDb().clone(-50000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondEqualizeDesiredMin.setStatus('current')
nbsSigCondEqualizeDesiredMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 22), NbsTcMilliDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondEqualizeDesiredMax.setStatus('current')
nbsSigCondEqualizeDesiredVal = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 23), NbsTcMilliDb().clone(-25000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondEqualizeDesiredVal.setStatus('current')
nbsSigCondRedundTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 227, 30, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondRedundTableSize.setStatus('current')
nbsSigCondRedundTable = MibTable((1, 3, 6, 1, 4, 1, 629, 227, 30, 2), )
if mibBuilder.loadTexts: nbsSigCondRedundTable.setStatus('current')
nbsSigCondRedundEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1), ).setIndexNames((0, "NBS-SIGCOND-MIB", "nbsSigCondRedundIfIndex"))
if mibBuilder.loadTexts: nbsSigCondRedundEntry.setStatus('current')
nbsSigCondRedundIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondRedundIfIndex.setStatus('current')
nbsSigCondRedundLimitMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1, 5), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondRedundLimitMin.setStatus('current')
nbsSigCondRedundLimitMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1, 8), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondRedundLimitMax.setStatus('current')
nbsSigCondRedundDesiredMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1, 10), NbsTcMilliDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondRedundDesiredMin.setStatus('current')
nbsSigCondRedundDesiredMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1, 15), NbsTcMilliDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondRedundDesiredMax.setStatus('current')
nbsSigCondPortTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 227, 40, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondPortTableSize.setStatus('current')
nbsSigCondPortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 227, 40, 2), )
if mibBuilder.loadTexts: nbsSigCondPortTable.setStatus('current')
nbsSigCondPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1), ).setIndexNames((0, "NBS-SIGCOND-MIB", "nbsSigCondPortIfIndex"))
if mibBuilder.loadTexts: nbsSigCondPortEntry.setStatus('current')
nbsSigCondPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsSigCondPortIfIndex.setStatus('current')
nbsSigCondPortRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondPortRxPower.setStatus('current')
nbsSigCondPortTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondPortTxPower.setStatus('current')
nbsSigCondPortReflection = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondPortReflection.setStatus('current')
nbsSigCondPortRxPowerMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondPortRxPowerMin.setStatus('current')
nbsSigCondPortRxPowerMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondPortRxPowerMax.setStatus('current')
nbsSigCondPortNoiseFigure = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondPortNoiseFigure.setStatus('current')
nbsSigCondChannelTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 227, 50, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondChannelTableSize.setStatus('current')
nbsSigCondChannelTable = MibTable((1, 3, 6, 1, 4, 1, 629, 227, 50, 2), )
if mibBuilder.loadTexts: nbsSigCondChannelTable.setStatus('current')
nbsSigCondChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1), ).setIndexNames((0, "NBS-SIGCOND-MIB", "nbsSigCondChannelIfIndex"), (0, "NBS-SIGCOND-MIB", "nbsSigCondChannelCenterline"))
if mibBuilder.loadTexts: nbsSigCondChannelEntry.setStatus('current')
nbsSigCondChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsSigCondChannelIfIndex.setStatus('current')
nbsSigCondChannelCenterline = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 2), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondChannelCenterline.setStatus('current')
nbsSigCondChannelRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 11), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondChannelRxPower.setStatus('current')
nbsSigCondChannelTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 12), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondChannelTxPower.setStatus('current')
nbsSigCondChannelTxAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 14), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondChannelTxAttenu.setStatus('current')
nbsSigCondChannelRxAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 15), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondChannelRxAttenu.setStatus('current')
nbsSigCondVodPortTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 227, 60, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVodPortTableSize.setStatus('current')
nbsSigCondVodPortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 227, 60, 2), )
if mibBuilder.loadTexts: nbsSigCondVodPortTable.setStatus('current')
nbsSigCondVodPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1), ).setIndexNames((0, "NBS-SIGCOND-MIB", "nbsSigCondVodPortIfIndex"))
if mibBuilder.loadTexts: nbsSigCondVodPortEntry.setStatus('current')
nbsSigCondVodPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsSigCondVodPortIfIndex.setStatus('current')
nbsSigCondVodPortDispersionMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionMin.setStatus('current')
nbsSigCondVodPortDispersionMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionMax.setStatus('current')
nbsSigCondVodPortDispersionAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionAdmin.setStatus('current')
nbsSigCondVodPortDispersionOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionOper.setStatus('current')
nbsSigCondVodPortDispersionGridOffsetCenter = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionGridOffsetCenter.setStatus('current')
nbsSigCondVodPortDispersionGridOffsetMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000)).clone(-100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionGridOffsetMin.setStatus('current')
nbsSigCondVodPortDispersionGridOffsetMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000)).clone(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionGridOffsetMax.setStatus('current')
nbsSigCondVodPortDispersionGridOffsetStep = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 13), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionGridOffsetStep.setStatus('current')
nbsSigCondVodPortDispersionGridOffsetExponent = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 14), Integer32().clone(9)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionGridOffsetExponent.setStatus('current')
nbsSigCondVodPortDispersionGridOffsetAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionGridOffsetAdmin.setStatus('current')
nbsSigCondVodPortDispersionGridOffsetOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100000, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSigCondVodPortDispersionGridOffsetOper.setStatus('current')
nbsSigCondEventEqualizeOk = NotificationType((1, 3, 6, 1, 4, 1, 629, 227, 200, 0, 20)).setObjects(("NBS-SIGCOND-MIB", "nbsSigCondEqualizeIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-SIGCOND-MIB", "nbsSigCondChannelCenterline"), ("NBS-SIGCOND-MIB", "nbsSigCondChannelTxPower"), ("NBS-SIGCOND-MIB", "nbsSigCondEqualizeDesiredMin"), ("NBS-SIGCOND-MIB", "nbsSigCondEqualizeDesiredMax"))
if mibBuilder.loadTexts: nbsSigCondEventEqualizeOk.setStatus('current')
nbsSigCondEventEqualizeTooLow = NotificationType((1, 3, 6, 1, 4, 1, 629, 227, 200, 0, 21)).setObjects(("NBS-SIGCOND-MIB", "nbsSigCondEqualizeIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-SIGCOND-MIB", "nbsSigCondChannelCenterline"), ("NBS-SIGCOND-MIB", "nbsSigCondChannelTxPower"), ("NBS-SIGCOND-MIB", "nbsSigCondEqualizeDesiredMin"))
if mibBuilder.loadTexts: nbsSigCondEventEqualizeTooLow.setStatus('current')
nbsSigCondEventEqualizeTooHigh = NotificationType((1, 3, 6, 1, 4, 1, 629, 227, 200, 0, 22)).setObjects(("NBS-SIGCOND-MIB", "nbsSigCondEqualizeIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-SIGCOND-MIB", "nbsSigCondChannelCenterline"), ("NBS-SIGCOND-MIB", "nbsSigCondChannelTxPower"), ("NBS-SIGCOND-MIB", "nbsSigCondEqualizeDesiredMax"))
if mibBuilder.loadTexts: nbsSigCondEventEqualizeTooHigh.setStatus('current')
mibBuilder.exportSymbols("NBS-SIGCOND-MIB", nbsSigCondRamanTableSize=nbsSigCondRamanTableSize, nbsSigCondRedundDesiredMin=nbsSigCondRedundDesiredMin, nbsSigCondVoaChannelRangeMin=nbsSigCondVoaChannelRangeMin, nbsSigCondPortTxPower=nbsSigCondPortTxPower, nbsSigCondPortTableSize=nbsSigCondPortTableSize, nbsSigCondChannelRxAttenu=nbsSigCondChannelRxAttenu, nbsSigCondChannelTxPower=nbsSigCondChannelTxPower, nbsSigCondVoaChannelRangeMax=nbsSigCondVoaChannelRangeMax, nbsSigCondVoaPortIfIndex=nbsSigCondVoaPortIfIndex, nbsSigCondEqualizeGrp=nbsSigCondEqualizeGrp, nbsSigCondVoaChannelRangeIncr=nbsSigCondVoaChannelRangeIncr, nbsSigCondEqualizeEntry=nbsSigCondEqualizeEntry, nbsSigCondPortEntry=nbsSigCondPortEntry, nbsSigCondPortGrp=nbsSigCondPortGrp, nbsSigCondChannelEntry=nbsSigCondChannelEntry, nbsSigCondChannelRxPower=nbsSigCondChannelRxPower, nbsSigCondChannelCenterline=nbsSigCondChannelCenterline, nbsSigCondEqualizeState=nbsSigCondEqualizeState, nbsSigCondVoaPortEntry=nbsSigCondVoaPortEntry, nbsSigCondPortNoiseFigure=nbsSigCondPortNoiseFigure, nbsSigCondRedundGrp=nbsSigCondRedundGrp, nbsSigCondVoaChannelRangeTableSize=nbsSigCondVoaChannelRangeTableSize, nbsSigCondChannelIfIndex=nbsSigCondChannelIfIndex, nbsSigCondVoaChannelRangeIfIndex=nbsSigCondVoaChannelRangeIfIndex, nbsSigCondVoaChannelRangeEntry=nbsSigCondVoaChannelRangeEntry, nbsSigCondRedundLimitMin=nbsSigCondRedundLimitMin, nbsSigCondEvent=nbsSigCondEvent, nbsSigCondPortTable=nbsSigCondPortTable, nbsSigCondChannelTxAttenu=nbsSigCondChannelTxAttenu, nbsSigCondVodPortTable=nbsSigCondVodPortTable, nbsSigCondEqualizeDesiredMax=nbsSigCondEqualizeDesiredMax, nbsSigCondVodPortTableSize=nbsSigCondVodPortTableSize, nbsSigCondMib=nbsSigCondMib, nbsSigCondVodPortDispersionGridOffsetCenter=nbsSigCondVodPortDispersionGridOffsetCenter, nbsSigCondRamanPumpPwrAdmin=nbsSigCondRamanPumpPwrAdmin, nbsSigCondVodPortGrp=nbsSigCondVodPortGrp, nbsSigCondEventEqualizeTooHigh=nbsSigCondEventEqualizeTooHigh, nbsSigCondEqualizeDesiredMin=nbsSigCondEqualizeDesiredMin, nbsSigCondRedundLimitMax=nbsSigCondRedundLimitMax, nbsSigCondChannelTable=nbsSigCondChannelTable, nbsSigCondRedundTableSize=nbsSigCondRedundTableSize, nbsSigCondChannelGrp=nbsSigCondChannelGrp, nbsSigCondVodPortDispersionGridOffsetExponent=nbsSigCondVodPortDispersionGridOffsetExponent, nbsSigCondVodPortDispersionOper=nbsSigCondVodPortDispersionOper, nbsSigCondEventEqualizeOk=nbsSigCondEventEqualizeOk, nbsSigCondVodPortIfIndex=nbsSigCondVodPortIfIndex, nbsSigCondRedundIfIndex=nbsSigCondRedundIfIndex, nbsSigCondEventEqualizeTooLow=nbsSigCondEventEqualizeTooLow, nbsSigCondVoaPortTableSize=nbsSigCondVoaPortTableSize, nbsSigCondEqualizeTableSize=nbsSigCondEqualizeTableSize, nbsSigCondVoaPortTxAttenuOper=nbsSigCondVoaPortTxAttenuOper, nbsSigCondVoaPortGrp=nbsSigCondVoaPortGrp, nbsSigCondRamanEntry=nbsSigCondRamanEntry, nbsSigCondVodPortDispersionAdmin=nbsSigCondVodPortDispersionAdmin, nbsSigCondVoaChannelGrp=nbsSigCondVoaChannelGrp, nbsSigCondRamanIfIndex=nbsSigCondRamanIfIndex, nbsSigCondVoaChannelRangeTable=nbsSigCondVoaChannelRangeTable, nbsSigCondRedundEntry=nbsSigCondRedundEntry, nbsSigCondRedundDesiredMax=nbsSigCondRedundDesiredMax, nbsSigCondVoaPortRxAttenuAdmin=nbsSigCondVoaPortRxAttenuAdmin, nbsSigCondVodPortEntry=nbsSigCondVodPortEntry, nbsSigCondVodPortDispersionGridOffsetMax=nbsSigCondVodPortDispersionGridOffsetMax, nbsSigCondEqualizeDesiredVal=nbsSigCondEqualizeDesiredVal, PYSNMP_MODULE_ID=nbsSigCondMib, nbsSigCondPortRxPower=nbsSigCondPortRxPower, nbsSigCondVoaPortRxAttenuOper=nbsSigCondVoaPortRxAttenuOper, nbsSigCondVoaPortTable=nbsSigCondVoaPortTable, nbsSigCondPortReflection=nbsSigCondPortReflection, nbsSigCondVodPortDispersionGridOffsetAdmin=nbsSigCondVodPortDispersionGridOffsetAdmin, nbsSigCondPortRxPowerMin=nbsSigCondPortRxPowerMin, nbsSigCondEqualizeLimitMax=nbsSigCondEqualizeLimitMax, nbsSigCondTraps=nbsSigCondTraps, nbsSigCondVodPortDispersionGridOffsetMin=nbsSigCondVodPortDispersionGridOffsetMin, nbsSigCondRamanGrp=nbsSigCondRamanGrp, nbsSigCondVoaPortTxAttenuAdmin=nbsSigCondVoaPortTxAttenuAdmin, nbsSigCondVodPortDispersionMax=nbsSigCondVodPortDispersionMax, nbsSigCondRamanTable=nbsSigCondRamanTable, nbsSigCondChannelTableSize=nbsSigCondChannelTableSize, nbsSigCondPortRxPowerMax=nbsSigCondPortRxPowerMax, nbsSigCondVodPortDispersionGridOffsetOper=nbsSigCondVodPortDispersionGridOffsetOper, nbsSigCondEqualizeLimitMin=nbsSigCondEqualizeLimitMin, nbsSigCondEqualizeIfIndex=nbsSigCondEqualizeIfIndex, nbsSigCondPortIfIndex=nbsSigCondPortIfIndex, nbsSigCondEqualizeTable=nbsSigCondEqualizeTable, nbsSigCondVodPortDispersionMin=nbsSigCondVodPortDispersionMin, nbsSigCondRedundTable=nbsSigCondRedundTable, nbsSigCondVodPortDispersionGridOffsetStep=nbsSigCondVodPortDispersionGridOffsetStep, nbsSigCondRamanPumpPwrOper=nbsSigCondRamanPumpPwrOper)
