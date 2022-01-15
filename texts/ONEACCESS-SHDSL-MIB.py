#
# PySNMP MIB module ONEACCESS-SHDSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oneaccess/ONEACCESS-SHDSL-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:19 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hdsl2ShdslSpanConfProfileEntry, hdsl2ShdslSpanStatusEntry, hdsl2ShdslEndpointCurrEntry = mibBuilder.importSymbols("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfProfileEntry", "hdsl2ShdslSpanStatusEntry", "hdsl2ShdslEndpointCurrEntry")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacExpIMSystem, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMSystem")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Integer32, ObjectIdentity, IpAddress, TimeTicks, MibIdentifier, iso, Counter64, Counter32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Integer32", "ObjectIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "iso", "Counter64", "Counter32", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacSHDSLMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3))
oacSHDSLMIBModule.setRevisions(('2011-06-15 00:00', '2010-08-20 00:01', '2010-07-30 00:01', '2010-07-08 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacSHDSLMIBModule.setRevisionsDescriptions(('This MIB module describes private extensions to the RFC4319 MIB.', 'Added oacSHDSLSpanConfProfileEocManagement,\n                       oacSHDSLSpanConfProfileEocStatusPollDelay and\n                       oacSHDSLSpanConfProfileEocStatusPollInterval.', 'Added oacSHDSLSpanConfProfileTable.', 'Initial version.',))
if mibBuilder.loadTexts: oacSHDSLMIBModule.setLastUpdated('201106150000Z')
if mibBuilder.loadTexts: oacSHDSLMIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacSHDSLMIBModule.setContactInfo('Pascal KESTELOOT\n            Postal: ONE ACCESS\n                    381 Avenue du General de Gaulle\n                    92140 Clamart, France\n\t\t    FRANCE\n\n            Tel: (+33) 01 41 87 70 00\n            Fax: (+33) 01 41 87 74 00\n\n            E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacSHDSLMIBModule.setDescription('Contact updated')
oacSHDSLObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1))
oacSHDSLSpanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2), )
if mibBuilder.loadTexts: oacSHDSLSpanStatusTable.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusTable.setDescription('This table provides overall status information of\n         HDSL2/SHDSL spans.  This table contains live data from\n         equipment.  As such, it is NOT persistent.')
oacSHDSLSpanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1), )
hdsl2ShdslSpanStatusEntry.registerAugmentions(("ONEACCESS-SHDSL-MIB", "oacSHDSLSpanStatusEntry"))
oacSHDSLSpanStatusEntry.setIndexNames(*hdsl2ShdslSpanStatusEntry.getIndexNames())
if mibBuilder.loadTexts: oacSHDSLSpanStatusEntry.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusEntry.setDescription('An entry in the oacSHDSLSpanStatusTable.  Each entry\n         represents the complete span in a single HDSL2/SHDSL line.\n         It is indexed by the ifIndex of the associated HDSL2/SHDSL\n         line.')
oacSHDSLSpanStatusUpDown = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusUpDown.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusUpDown.setDescription('Contains the Global Up/Down Counter for the span.')
oacSHDSLSpanStatusCurrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(30, 30)).setFixedLength(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrStatus.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrStatus.setDescription('Contains the current G.SHDSL Status.')
oacSHDSLSpanStatusCurrShowtimeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrShowtimeStart.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrShowtimeStart.setDescription('Contains the current Showtime Start.')
oacSHDSLSpanStatusCurrCellDelin = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrCellDelin.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrCellDelin.setDescription('Contains the current Cell Delin counter.')
oacSHDSLSpanStatusCurrCRCanomalies = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrCRCanomalies.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrCRCanomalies.setDescription('Contains the current CRC counter.')
oacSHDSLSpanStatusCurrHECErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrHECErrors.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrHECErrors.setDescription('Contains the current HEC counter.')
oacSHDSLSpanStatusCurrRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrRxCells.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrRxCells.setDescription('Contains the current Rx Cells counter.')
oacSHDSLSpanStatusCurrTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrTxCells.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrTxCells.setDescription('Contains the current Tx Cells counter.')
oacSHDSLSpanStatusCurrRxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrRxDrops.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrRxDrops.setDescription('Contains the current Rx Drops counter.')
oacSHDSLSpanStatusCurrES = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrES.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrES.setDescription('Contains the current ES counter.')
oacSHDSLSpanStatusCurrSES = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrSES.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrSES.setDescription('Contains the current SES counter.')
oacSHDSLSpanStatusCurrLOSWS = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrLOSWS.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrLOSWS.setDescription('Contains the current LOSWS counter.')
oacSHDSLSpanStatusCurrUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrUAS.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrUAS.setDescription('Contains the current UAS counter.')
oacSHDSLSpanStatusCurrConstellation = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("tcPam16", 2), ("tcPam32", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrConstellation.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrConstellation.setDescription('The current constellation (line coding) for the span.')
oacSHDSLEndpointCurrTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5), )
if mibBuilder.loadTexts: oacSHDSLEndpointCurrTable.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrTable.setDescription('This table contains current status and performance information\n         for segment endpoints in HDSL2/SHDSL lines.  As with other\n         tables in this MIB module indexed by ifIndex, entries in this\n         table MUST be maintained in a persistent manner.')
oacSHDSLEndpointCurrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1), )
hdsl2ShdslEndpointCurrEntry.registerAugmentions(("ONEACCESS-SHDSL-MIB", "oacSHDSLEndpointCurrEntry"))
oacSHDSLEndpointCurrEntry.setIndexNames(*hdsl2ShdslEndpointCurrEntry.getIndexNames())
if mibBuilder.loadTexts: oacSHDSLEndpointCurrEntry.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrEntry.setDescription('Defines an entry in the oacSHDSLEndpointCurrTable.')
oacSHDSLEndpointCurrAtn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1270, 1280))).setUnits('dB/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrAtn.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrAtn.setDescription('The current loop attenuation for this endpoint as reported in\n         a Network or Customer Side Performance Status message. In tenths of dB.')
oacSHDSLEndpointCurrSnrMgn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1270, 1280))).setUnits('dB/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrSnrMgn.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrSnrMgn.setDescription('The current SNR margin for this endpoint as reported in a\n         Status Response/SNR message. In tenths of dB.')
oacSHDSLEndpointCurrTxPwr = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 3), Integer32()).setUnits('dB/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrTxPwr.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrTxPwr.setDescription('The current transmit power for this endpoint. In tenths of dB.')
oacSHDSLEndpointCurrRxGain = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 4), Integer32()).setUnits('dB/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrRxGain.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrRxGain.setDescription('The current receiver gain for this endpoint. In tenths of dB.')
oacSHDSLEndpointCurrMaxAttainableLineRate = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrMaxAttainableLineRate.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrMaxAttainableLineRate.setDescription('The current Max Attainable LineRate for this endpoint.')
oacSHDSLEndpointCurrCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrCommands.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrCommands.setDescription('The current Commands for this endpoint.')
oacSHDSLEndpointCurrResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrResponses.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrResponses.setDescription('The current Responses for this endpoint.')
oacSHDSLEndpointCurrdiscardedCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrdiscardedCommands.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrdiscardedCommands.setDescription('The current discarded Commands for this endpoint.')
oacSHDSLEndpointCurrerroredCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrerroredCommands.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrerroredCommands.setDescription('The current errored Commands for this endpoint.')
oacSHDSLEndpointCurrReceivedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrReceivedFrames.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrReceivedFrames.setDescription('The current Received Frames for this endpoint.')
oacSHDSLEndpointCurrBadTransparency = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrBadTransparency.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrBadTransparency.setDescription('The current Bad Transparency for this endpoint.')
oacSHDSLEndpointCurrBadFCS = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrBadFCS.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrBadFCS.setDescription('The current Bad FCS for this endpoint.')
oacSHDSLEndpointCurrEOCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50)).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrEOCStatus.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrEOCStatus.setDescription('The current EOC Status for this endpoint.')
oacSHDSLEndpointCurrretrainTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7), )
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainTable.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainTable.setDescription('This table contains current status and performance information\n         for segment endpoints in HDSL2/SHDSL lines.  As with other\n         tables in this MIB module indexed by ifIndex, entries in this\n         table MUST be maintained in a persistent manner.')
oacSHDSLEndpointCurrretrainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1), )
hdsl2ShdslEndpointCurrEntry.registerAugmentions(("ONEACCESS-SHDSL-MIB", "oacSHDSLEndpointCurrretrainEntry"))
oacSHDSLEndpointCurrretrainEntry.setIndexNames(*hdsl2ShdslEndpointCurrEntry.getIndexNames())
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainEntry.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainEntry.setDescription('Defines an entry in the oacSHDSLEndpointCurrretrainTable.')
oacSHDSLEndpointCurrretrainSQPAIR = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 1), Integer32()).setUnits('SQPAIR').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainSQPAIR.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainSQPAIR.setDescription('The current retrain SQ for this endpoint as reported in\n         a Network or Customer Side Performance Status message.')
oacSHDSLEndpointCurrretrainSQLINE = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 2), Integer32()).setUnits('SQLINE').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainSQLINE.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainSQLINE.setDescription('The current retrain SQ for this endpoint as reported in\n         a Network or Customer Side Performance Status message.')
oacSHDSLEndpointCurrretrainCRCPAIR = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 3), Integer32()).setUnits('CRCPAIR').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainCRCPAIR.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainCRCPAIR.setDescription('The current retrain CRC for this endpoint as reported in\n         a Network or Customer Side Performance Status message.')
oacSHDSLEndpointCurrretrainCRCLINE = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 4), Integer32()).setUnits('CRCLINE').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainCRCLINE.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainCRCLINE.setDescription('The current retrain CRC for this endpoint as reported in\n         a Network or Customer Side Performance Status message.')
oacSHDSLEndpointCurrretrainFsyncPAIR = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 5), Integer32()).setUnits('FsyncPAIR').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFsyncPAIR.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFsyncPAIR.setDescription('The current retrain Fsync for this endpoint as reported in\n         a Network or Customer Side Performance Status message.')
oacSHDSLEndpointCurrretrainFsyncLINE = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 6), Integer32()).setUnits('FsyncLINE').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFsyncLINE.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFsyncLINE.setDescription('The current retrain Fsync for this endpoint as reported in\n         a Network or Customer Side Performance Status message.')
oacSHDSLEndpointCurrretrainFSyncSQPAIR = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 7), Integer32()).setUnits('FSync&SQPAIR').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFSyncSQPAIR.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFSyncSQPAIR.setDescription('The current retrain FSync&SQ for this endpoint as reported in\n         a Network or Customer Side Performance Status message.')
oacSHDSLEndpointCurrretrainFSyncSQLINE = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 8), Integer32()).setUnits('FSync&SQLINE').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFSyncSQLINE.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFSyncSQLINE.setDescription('The current retrain FSync&SQ for this endpoint as reported in\n         a Network or Customer Side Performance Status message.')
oacSHDSLTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 2))
oacSHDSLTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 2, 0))
oacSHDSLHardDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 2, 0, 1))
if mibBuilder.loadTexts: oacSHDSLHardDownTrap.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLHardDownTrap.setDescription('this notification indicate that the shdsl line speed is lower than the threshold configured in efm interface. \n  as consequence, the interface ethernet which the hard-down option is enable will be shutdown, \nit will be UP if the shdsl line recovered the good linerate.')
oacSHDSLSpanConfProfileTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10), )
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileTable.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileTable.setDescription('This table supports definitions of span configuration\n         profiles for SHDSL lines.  This table MUST be maintained\n         in a persistent manner')
oacSHDSLSpanConfProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1), )
hdsl2ShdslSpanConfProfileEntry.registerAugmentions(("ONEACCESS-SHDSL-MIB", "oacSHDSLSpanConfProfileEntry"))
oacSHDSLSpanConfProfileEntry.setIndexNames(*hdsl2ShdslSpanConfProfileEntry.getIndexNames())
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEntry.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEntry.setDescription('Each entry corresponds to a single span configuration\n         profile.  Each profile contains a set of span configuration\n         parameters.  The configuration parameters in a profile are\n         applied to those lines referencing that profile (see the\n         hdsl2ShdslSpanConfProfile object).  ')
oacSHDSLSpanConfProfileConstellation = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("tcPam16", 2), ("tcPam32", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileConstellation.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileConstellation.setDescription('The configured constellation (line coding) for the span.\n         Corresponds to cli command (controller shdsl 0, dsl-group 0):\n         annex ... tc-pam <value>')
oacSHDSLSpanConfProfileAutoConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileAutoConfig.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileAutoConfig.setDescription('The configured auto configuration mode (enabled or disabled) for the span.\n         Corresponds to cli command (controller shdsl 0, dsl-group 0):\n            autoconfig / no autoconfig')
oacSHDSLSpanConfProfileCaplist = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("newstyle", 1), ("oldstyle", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileCaplist.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileCaplist.setDescription('The configured capability list style for the span.\n         Corresponds to cli command (controller shdsl 0, dsl-group 0):\n            caplist <value>')
oacSHDSLSpanConfProfileEfmAggregation = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("auto", 2), ("negotiated", 3), ("static", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEfmAggregation.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEfmAggregation.setDescription('The configured efm aggregation mode for the span.\n         Corresponds to cli command (controller shdsl 0, dsl-group 0):\n            efmaggregation <value>')
oacSHDSLSpanConfProfileCrcCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileCrcCheck.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileCrcCheck.setDescription('The configured numbered of consecutive seconds with crc errors after which the link will be retrained.\n         If the value is set to 0, than no retrain will occur based on crc errors.\n         Corresponds to cli command (controller shdsl 0, dsl-group 0):\n            value 0 :         crc no \n            all other values: crc check <value> ')
oacSHDSLSpanConfProfileMeansqCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileMeansqCheck.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileMeansqCheck.setDescription('The configured numbered of consecutive seconds where the noise margin is below \n         the configured threshold (oacSHDSLSpanConfProfileMeansqThreshold) after which the link will be retrained.\n         If the value is set to 0, than no retrain will occur based on noise margin verification.\n         Corresponds to cli command (controller shdsl 0, dsl-group 0):\n            value 0 :         meansq no \n            all other values: meansq check <value> ')
oacSHDSLSpanConfProfileMeansqThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileMeansqThreshold.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileMeansqThreshold.setDescription('The configured threshold (in dB) for retrain check based on the noise margin.\n        If the noise margin drops below the configured threshold for the configured time\n        (oacSHDSLSpanConfProfileMeansqCheck) than the link will be retrained.\n         Corresponds to cli command (controller shdsl 0, dsl-group 0):\n            meansq check <time> <value> ')
oacSHDSLSpanConfProfileLineProbing = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adaptive", 1), ("normal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileLineProbing.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileLineProbing.setDescription("The configured linprobing mechanism. \n         - normal corresponds to the standard line probing (pmms) as defined in the standard (G.991.2).\n         - adaptive has to be used in situations where there is cross-talk between the lines of the same span.\n           A propriatary algorithm will be activated that will limit the maximum speed if the normal line probing\n           mechanism cannot reach a stable sync due to it's limitations (cross-talk is not taken into account in the \n           standard line probing mechanism). The disadvantage of the adaptive mode is that it can take a long time \n           before a stable sync is reached.\n        \n        Corresponds to cli command (controller shdsl 0, dsl-group 0):\n            lineprobing <value> ")
oacSHDSLSpanConfProfileEocManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEocManagement.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEocManagement.setDescription('This object enables/disables the EOC management of the SHDSL line in this unit.')
oacSHDSLSpanConfProfileEocStatusPollDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 29))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEocStatusPollDelay.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEocStatusPollDelay.setDescription('The delay in seconds after the start of the full quarter of an hour when an EOC full status request\n        is sent to the devices in the span. Periodically after this start point full status request will\n        be sent with a configured interval (oacSHDSLSpanConfProfileEocStatusPollInterval).')
oacSHDSLSpanConfProfileEocStatusPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(30, 30), ValueRangeConstraint(60, 60), ValueRangeConstraint(90, 90), ValueRangeConstraint(120, 120), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEocStatusPollInterval.setStatus('current')
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEocStatusPollInterval.setDescription('The delay in seconds between 2 EOC full status requests to the same device in the shdsl span.')
mibBuilder.exportSymbols("ONEACCESS-SHDSL-MIB", oacSHDSLSpanStatusCurrUAS=oacSHDSLSpanStatusCurrUAS, oacSHDSLSpanStatusCurrCellDelin=oacSHDSLSpanStatusCurrCellDelin, oacSHDSLEndpointCurrResponses=oacSHDSLEndpointCurrResponses, oacSHDSLEndpointCurrretrainSQPAIR=oacSHDSLEndpointCurrretrainSQPAIR, oacSHDSLEndpointCurrTable=oacSHDSLEndpointCurrTable, oacSHDSLHardDownTrap=oacSHDSLHardDownTrap, oacSHDSLSpanStatusCurrShowtimeStart=oacSHDSLSpanStatusCurrShowtimeStart, oacSHDSLEndpointCurrretrainCRCPAIR=oacSHDSLEndpointCurrretrainCRCPAIR, oacSHDSLEndpointCurrretrainFSyncSQPAIR=oacSHDSLEndpointCurrretrainFSyncSQPAIR, oacSHDSLSpanStatusEntry=oacSHDSLSpanStatusEntry, oacSHDSLEndpointCurrretrainEntry=oacSHDSLEndpointCurrretrainEntry, oacSHDSLEndpointCurrretrainSQLINE=oacSHDSLEndpointCurrretrainSQLINE, oacSHDSLTraps=oacSHDSLTraps, oacSHDSLSpanStatusCurrCRCanomalies=oacSHDSLSpanStatusCurrCRCanomalies, oacSHDSLEndpointCurrretrainTable=oacSHDSLEndpointCurrretrainTable, oacSHDSLSpanConfProfileEocStatusPollDelay=oacSHDSLSpanConfProfileEocStatusPollDelay, oacSHDSLEndpointCurrEOCStatus=oacSHDSLEndpointCurrEOCStatus, oacSHDSLEndpointCurrSnrMgn=oacSHDSLEndpointCurrSnrMgn, oacSHDSLSpanStatusCurrConstellation=oacSHDSLSpanStatusCurrConstellation, oacSHDSLSpanConfProfileMeansqThreshold=oacSHDSLSpanConfProfileMeansqThreshold, oacSHDSLSpanConfProfileEocManagement=oacSHDSLSpanConfProfileEocManagement, oacSHDSLSpanConfProfileTable=oacSHDSLSpanConfProfileTable, oacSHDSLSpanStatusCurrRxCells=oacSHDSLSpanStatusCurrRxCells, oacSHDSLSpanStatusCurrES=oacSHDSLSpanStatusCurrES, oacSHDSLEndpointCurrTxPwr=oacSHDSLEndpointCurrTxPwr, oacSHDSLEndpointCurrerroredCommands=oacSHDSLEndpointCurrerroredCommands, oacSHDSLEndpointCurrMaxAttainableLineRate=oacSHDSLEndpointCurrMaxAttainableLineRate, oacSHDSLSpanStatusCurrRxDrops=oacSHDSLSpanStatusCurrRxDrops, oacSHDSLEndpointCurrAtn=oacSHDSLEndpointCurrAtn, oacSHDSLSpanStatusCurrLOSWS=oacSHDSLSpanStatusCurrLOSWS, oacSHDSLEndpointCurrretrainFsyncLINE=oacSHDSLEndpointCurrretrainFsyncLINE, oacSHDSLSpanStatusCurrHECErrors=oacSHDSLSpanStatusCurrHECErrors, oacSHDSLSpanConfProfileEocStatusPollInterval=oacSHDSLSpanConfProfileEocStatusPollInterval, oacSHDSLEndpointCurrdiscardedCommands=oacSHDSLEndpointCurrdiscardedCommands, oacSHDSLEndpointCurrretrainFSyncSQLINE=oacSHDSLEndpointCurrretrainFSyncSQLINE, oacSHDSLSpanConfProfileCrcCheck=oacSHDSLSpanConfProfileCrcCheck, oacSHDSLEndpointCurrBadTransparency=oacSHDSLEndpointCurrBadTransparency, oacSHDSLSpanConfProfileLineProbing=oacSHDSLSpanConfProfileLineProbing, oacSHDSLSpanStatusCurrStatus=oacSHDSLSpanStatusCurrStatus, oacSHDSLSpanConfProfileCaplist=oacSHDSLSpanConfProfileCaplist, oacSHDSLSpanConfProfileMeansqCheck=oacSHDSLSpanConfProfileMeansqCheck, oacSHDSLEndpointCurrReceivedFrames=oacSHDSLEndpointCurrReceivedFrames, oacSHDSLSpanStatusUpDown=oacSHDSLSpanStatusUpDown, oacSHDSLEndpointCurrBadFCS=oacSHDSLEndpointCurrBadFCS, oacSHDSLObjects=oacSHDSLObjects, PYSNMP_MODULE_ID=oacSHDSLMIBModule, oacSHDSLSpanConfProfileConstellation=oacSHDSLSpanConfProfileConstellation, oacSHDSLSpanConfProfileEfmAggregation=oacSHDSLSpanConfProfileEfmAggregation, oacSHDSLSpanConfProfileAutoConfig=oacSHDSLSpanConfProfileAutoConfig, oacSHDSLSpanStatusCurrTxCells=oacSHDSLSpanStatusCurrTxCells, oacSHDSLEndpointCurrEntry=oacSHDSLEndpointCurrEntry, oacSHDSLEndpointCurrCommands=oacSHDSLEndpointCurrCommands, oacSHDSLSpanStatusCurrSES=oacSHDSLSpanStatusCurrSES, oacSHDSLEndpointCurrRxGain=oacSHDSLEndpointCurrRxGain, oacSHDSLEndpointCurrretrainCRCLINE=oacSHDSLEndpointCurrretrainCRCLINE, oacSHDSLMIBModule=oacSHDSLMIBModule, oacSHDSLEndpointCurrretrainFsyncPAIR=oacSHDSLEndpointCurrretrainFsyncPAIR, oacSHDSLTrapPrefix=oacSHDSLTrapPrefix, oacSHDSLSpanStatusTable=oacSHDSLSpanStatusTable, oacSHDSLSpanConfProfileEntry=oacSHDSLSpanConfProfileEntry)
