#
# PySNMP MIB module SIAE-HITLESS-AGGRL1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-HITLESS-AGGRL1-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:34:26 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
aggrL1Entry, = mibBuilder.importSymbols("SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1Entry")
linkStatusEntry, linkSettingsEntry = mibBuilder.importSymbols("SIAE-RADIO-SYSTEM-MIB", "linkStatusEntry", "linkSettingsEntry")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Integer32, TimeTicks, MibIdentifier, iso, Counter32, Gauge32, ModuleIdentity, Counter64, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Integer32", "TimeTicks", "MibIdentifier", "iso", "Counter32", "Gauge32", "ModuleIdentity", "Counter64", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hitlessAggregationL1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 98))
hitlessAggregationL1.setRevisions(('2016-02-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hitlessAggregationL1.setRevisionsDescriptions(('Initial version 01.00.00.\n            ',))
if mibBuilder.loadTexts: hitlessAggregationL1.setLastUpdated('201602290000Z')
if mibBuilder.loadTexts: hitlessAggregationL1.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: hitlessAggregationL1.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: hitlessAggregationL1.setDescription('This module contains the hitless extension for a Level 1\n             aggregations of SIAE equipments.\n\n             The Hitless L1 aggregation is a method to define radio link\n             degradation in order to remove it from aggregation in advance\n             (link status estimator).\n             Only ethernet traffic is affected.\n\n             The current TX profile of a link is used as extimator of the\n             link status. When ACM modulation goes under a predefined profile\n             (configurable by operator) the corresponding link is removed from\n             RLAG. A radio link is considered unavailable for ethernet traffic\n             during all the time that the current modulation remain under\n             the predefined HITLESS profile (modulation). \n\n             Every radio link is considered working in three separate ZONEs\n             - GOOD ZONE: When it is working between the HITLESS profile\n                          (included) and the UPPER profile (included) \n             - HITLESS ZONE: When it is working between the LOWER profile \n                             (included) and the HITLESS profile (excluded)\n             - BAD ZONE: When the modem is unlocked\n\n             NE is in charge to select which of the links, that are working into\n             the HITLESS ZONE, participate in RLAG. The decision is taken \n             according to three possible behaviors:\n             - ALL survive:  All links remain used by aggregator when working\n                             into the HITLESS ZONE\n             - ONE survive:  When NO link is working into the GOOD ZONE,\n                             the last link entered into the HITLESS ZONE\n                             continues to be used by the aggregator \n             - NONE survive: Each link is removed from aggregation when working\n                             into the HITLESS ZONE\n\n             Note that when HITLESS profile is configured equal to the LOWER \n             profile, the ONE survive and NONE survive behave like the ALL\n             survive. \n            ')
hlAggrL1MibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hlAggrL1MibVersion.setStatus('current')
if mibBuilder.loadTexts: hlAggrL1MibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
hlAggrL1Table = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 2), )
if mibBuilder.loadTexts: hlAggrL1Table.setStatus('current')
if mibBuilder.loadTexts: hlAggrL1Table.setDescription('A list of hitless L1 aggregation (RLAG) entries.\n            ')
hlAggrL1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 2, 1), )
aggrL1Entry.registerAugmentions(("SIAE-HITLESS-AGGRL1-MIB", "hlAggrL1Entry"))
hlAggrL1Entry.setIndexNames(*aggrL1Entry.getIndexNames())
if mibBuilder.loadTexts: hlAggrL1Entry.setStatus('current')
if mibBuilder.loadTexts: hlAggrL1Entry.setDescription('An entry containing management information applicable to the  \n             hitless extension for L1 aggregation.\n            ')
hlAggrL1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hlAggrL1Auto", 1), ("hlAggrL1Manual", 2))).clone('hlAggrL1Auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hlAggrL1Mode.setStatus('current')
if mibBuilder.loadTexts: hlAggrL1Mode.setDescription('This object defines how the HITLESS profiles is choosen (HITLESS\n            profile is last profile that is considered good for L1 agrregation):\n\n            hlAggrL1Auto(1):   NE uses linkTxLowerProfile+1 as HITLESS profile\n            hlAggrL1Manual(2): NE uses the values set in hlLinkSettingsTable\n                               as HITLESS profile \n           ')
hlAggrL1Behaviour = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hlAggrL1AllSurvive", 1), ("hlAggrL1OneSurvive", 2), ("hlAggrL1NoneSurvive", 3))).clone('hlAggrL1AllSurvive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hlAggrL1Behaviour.setStatus('current')
if mibBuilder.loadTexts: hlAggrL1Behaviour.setDescription('Every radio link is considered working in three separate ZONEs:\n             GOOD ZONE:    When it is working between the HITLESS profile\n                           (included) and the UPPER profile (included) \n             HITLESS ZONE: When it is working between the LOWER profile \n                           (included) and the HITLESS profile (excluded)\n             BAD ZONE:     When the modem is unlocked\n\n             HITLESS profile (one for each radio link) is last profile that\n             is considered good for L1 aggregation.\n\n             NE is in charge to select which of the links that are working\n             into the HITLESS ZONE participate in L1 aggregation. The decision\n             is taken according to three possible behaviors:\n\n             hlAggrL1AllSurvive(1):  All links remain used by aggregator when\n                                     working into the HITLESS ZONE.\n             hlAggrL1OneSurvive(2):  When NO link is working into the GOOD ZONE,\n                                     the last link entered into the HITLESS ZONE\n                                     continues to be used by the aggregator \n             hlAggrL1NoneSurvive(3): Each link is removed from aggregation when\n                                     working into the HITLESS ZONE\n            ')
hlLinkSettingsTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 3), )
if mibBuilder.loadTexts: hlLinkSettingsTable.setStatus('current')
if mibBuilder.loadTexts: hlLinkSettingsTable.setDescription('Table with the hitless L1 aggregation extension of \n             linkSettingsEntry. The content of this table can be changed by a\n             manager if linkRowStatus is notInService(2).\n            ')
hlLinkSettingsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 3, 1), )
linkSettingsEntry.registerAugmentions(("SIAE-HITLESS-AGGRL1-MIB", "hlLinkSettingsEntry"))
hlLinkSettingsEntry.setIndexNames(*linkSettingsEntry.getIndexNames())
if mibBuilder.loadTexts: hlLinkSettingsEntry.setStatus('current')
if mibBuilder.loadTexts: hlLinkSettingsEntry.setDescription('An entry containing the hitless L1 aggregation extension of \n             linkSettingsEntry.\n           .')
linkHitlessProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 3, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: linkHitlessProfile.setStatus('current')
if mibBuilder.loadTexts: linkHitlessProfile.setDescription('The object contains hitless profile that is used to remove the\n              radio link from the L1 aggregation.\n             ')
hlLinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 4), )
if mibBuilder.loadTexts: hlLinkStatusTable.setStatus('current')
if mibBuilder.loadTexts: hlLinkStatusTable.setDescription('Table with hitless L1 aggregation extension of linkStatusEntry.\n            ')
hlLinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 4, 1), )
linkStatusEntry.registerAugmentions(("SIAE-HITLESS-AGGRL1-MIB", "hlLinkStatusEntry"))
hlLinkStatusEntry.setIndexNames(*linkStatusEntry.getIndexNames())
if mibBuilder.loadTexts: hlLinkStatusEntry.setStatus('current')
if mibBuilder.loadTexts: hlLinkStatusEntry.setDescription('An entry containing the hitless L1 aggregation extension of\n             linkStatusEntry.\n            ')
linkHitlessZone = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 98, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("goodZone", 1), ("hitlessZone", 2), ("badZone", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkHitlessZone.setStatus('current')
if mibBuilder.loadTexts: linkHitlessZone.setDescription('The object shows the working zone of an aggregated radio\n             link.\n            ')
mibBuilder.exportSymbols("SIAE-HITLESS-AGGRL1-MIB", hlAggrL1Behaviour=hlAggrL1Behaviour, hitlessAggregationL1=hitlessAggregationL1, hlAggrL1Entry=hlAggrL1Entry, hlAggrL1Table=hlAggrL1Table, hlAggrL1Mode=hlAggrL1Mode, linkHitlessZone=linkHitlessZone, hlLinkStatusEntry=hlLinkStatusEntry, linkHitlessProfile=linkHitlessProfile, PYSNMP_MODULE_ID=hitlessAggregationL1, hlLinkStatusTable=hlLinkStatusTable, hlLinkSettingsTable=hlLinkSettingsTable, hlAggrL1MibVersion=hlAggrL1MibVersion, hlLinkSettingsEntry=hlLinkSettingsEntry)
