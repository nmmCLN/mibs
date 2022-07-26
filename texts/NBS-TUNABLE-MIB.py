#
# PySNMP MIB module NBS-TUNABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-TUNABLE-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:31:34 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, Unsigned32, Counter64, IpAddress, Integer32, ModuleIdentity, MibIdentifier, NotificationType, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Unsigned32", "Counter64", "IpAddress", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsTunableMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 203))
if mibBuilder.loadTexts: nbsTunableMib.setLastUpdated('201706280000Z')
if mibBuilder.loadTexts: nbsTunableMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsTunableMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsTunableMib.setDescription('MIB for representing Tunable Optics parameters')
nbsTunableGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 203, 1))
if mibBuilder.loadTexts: nbsTunableGrp.setStatus('current')
if mibBuilder.loadTexts: nbsTunableGrp.setDescription('MIB for representing Tunable Optics parameters')
nbsTunableChannelTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 203, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelTableSize.setDescription('The number of entries in nbsTunableChannelTable.')
nbsTunableChannelTable = MibTable((1, 3, 6, 1, 4, 1, 629, 203, 1, 2), )
if mibBuilder.loadTexts: nbsTunableChannelTable.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelTable.setDescription('A table to report and configure tunable optics settings.')
nbsTunableChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1), ).setIndexNames((0, "NBS-TUNABLE-MIB", "nbsTunableChannelIfIndex"))
if mibBuilder.loadTexts: nbsTunableChannelEntry.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelEntry.setDescription("Describes a setting for an interface's tunable optics.")
nbsTunableChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelIfIndex.setDescription("The Mib2 ifIndex of this optic's port")
nbsTunableChannelFreqStart = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 2), Integer32().clone(190100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqStart.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqStart.setDescription("The first allowable frequency for this tunable optic, in\n           GigaHertz (GHz), unless FreqExponent != 9.\n\n           For L-Band, ITU Grid 48 is '184800'\n           For Q-Band, ITU Grid 48 is '184850'\n           For C-Band, ITU Grid 1 is '190100'\n           For H-Band, ITU Grid 1 is '190150'\n\n           If GHz does not provide the appropriate resolution, the\n           tunable optic may report a FreqExponent less than 9.\n\n           If 32 bits is insufficient to cover the range in GHz, the\n           tunable optic may report a FreqExponent greater than 9.\n\n           Not supported value: 0")
nbsTunableChannelFreqEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 3), Integer32().clone(197200)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqEnd.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqEnd.setDescription("The last allowable frequency (inclusive) for this tunable\n           optic, in GigaHertz (GHz), unless FreqExponent != 9.\n\n           For L-Band, ITU Grid 99 is '189900'\n           For Q-Band, ITU Grid 99 is '189950'\n           For C-Band, ITU Grid 72 is '197200'\n           For H-Band, ITU Grid 72 is '197250'\n\n           If GHz does not provide the appropriate resolution, the\n           tunable optic may report a FreqExponent less than 9.\n\n           If 32 bits is insufficient to cover the range in GHz, the\n           tunable optic may report a FreqExponent greater than 9.\n\n           Not supported value: 0")
nbsTunableChannelFreqStep = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 4), Integer32().clone(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqStep.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqStep.setDescription('The spacing of the allowable frequencies that this tunable\n           optic supports, in GigaHertz (GHz), unless FreqExponent != 9.\n\n           100 indicates the standard ITU grid spacing of 100GHz.\n\n           For example, if this tunable optic supports both C and H\n           band, or both Q and L band, FreqStep should report 50.\n\n           If this tunable optic supports steps finer than 1GHz,\n           the tunable optic may report a FreqExponent less than 9.\n\n           Not supported value: 0')
nbsTunableChannelFreqExponent = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 5), Integer32().clone(9)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqExponent.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqExponent.setDescription('The exponent of all the Freq values (including FreqStep). 9\n           (the default) indicates all units are in GigaHertz (GHz).')
nbsTunableChannelFreqAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsTunableChannelFreqAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqAdmin.setDescription('The administratively desired frequency of this tunable\n           optic, in GigaHertz (GHz), unless FreqExponent != 9.\n\n           Not supported value: 0')
nbsTunableChannelFreqOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqOper.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqOper.setDescription('The current operational frequency of this tunable\n           optic, in GigaHertz (GHz), unless FreqExponent != 9.\n\n           Not supported value: 0')
nbsTunableChannelFreqDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqDefault.setStatus('current')
if mibBuilder.loadTexts: nbsTunableChannelFreqDefault.setDescription('The default frequency of this tunable optic, in GigaHertz\n           (GHz), unless FreqExponent != 9.\n\n           Not supported value: 0')
mibBuilder.exportSymbols("NBS-TUNABLE-MIB", nbsTunableMib=nbsTunableMib, nbsTunableChannelFreqEnd=nbsTunableChannelFreqEnd, nbsTunableChannelFreqOper=nbsTunableChannelFreqOper, nbsTunableChannelEntry=nbsTunableChannelEntry, nbsTunableChannelFreqExponent=nbsTunableChannelFreqExponent, nbsTunableChannelFreqStep=nbsTunableChannelFreqStep, nbsTunableChannelFreqDefault=nbsTunableChannelFreqDefault, nbsTunableGrp=nbsTunableGrp, nbsTunableChannelTableSize=nbsTunableChannelTableSize, nbsTunableChannelIfIndex=nbsTunableChannelIfIndex, nbsTunableChannelFreqAdmin=nbsTunableChannelFreqAdmin, nbsTunableChannelTable=nbsTunableChannelTable, PYSNMP_MODULE_ID=nbsTunableMib, nbsTunableChannelFreqStart=nbsTunableChannelFreqStart)
