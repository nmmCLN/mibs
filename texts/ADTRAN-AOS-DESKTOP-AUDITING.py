#
# PySNMP MIB module ADTRAN-AOS-DESKTOP-AUDITING (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-DESKTOP-AUDITING
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:39 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
adGenAOSConformance, adGenAOSSwitch = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSSwitch")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, NotificationType, ObjectIdentity, Bits, iso, IpAddress, Integer32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Bits", "iso", "IpAddress", "Integer32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention, DateAndTime, TruthValue, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime", "TruthValue", "TimeStamp")
adGenAOSDesktopAuditingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 4, 1))
if mibBuilder.loadTexts: adGenAOSDesktopAuditingMib.setLastUpdated('200912140000Z')
if mibBuilder.loadTexts: adGenAOSDesktopAuditingMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSDesktopAuditingMib.setContactInfo('Technical Support Dept.\n                Postal: ADTRAN, Inc.\n                901 Explorer Blvd.\n                Huntsville, AL 35806\n\n                Tel: +1 800 726-8663\n                Fax: +1 256 963 6217\n                E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSDesktopAuditingMib.setDescription('First Draft of ADTRAN-AOS-DESKTOP-AUDITING MIB module.')
adGenDesktopAuditing = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2))
adGenNapClients = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0))
adGenNapClientsTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1), )
if mibBuilder.loadTexts: adGenNapClientsTable.setStatus('current')
if mibBuilder.loadTexts: adGenNapClientsTable.setDescription('The NAP client table displays NAP information of NAP capable clients.  It displays information \n            such as clients firewall, antivirus, antispyware, and security states.  ')
adGenNapClientsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1), ).setIndexNames((0, "ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientMac"), (0, "ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientVlanId"))
if mibBuilder.loadTexts: adGenNapClientsEntry.setStatus('current')
if mibBuilder.loadTexts: adGenNapClientsEntry.setDescription('NAP information of the client')
adNapClientMac = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientMac.setStatus('current')
if mibBuilder.loadTexts: adNapClientMac.setDescription('NAP clients MAC address. This is unique to the Desktop Auditing MIB.')
adNapClientVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientVlanId.setStatus('current')
if mibBuilder.loadTexts: adNapClientVlanId.setDescription('NAP clients VLAN ID. This ID is unique to the Desktop Auditing MIB.')
adNapClientIp = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientIp.setStatus('current')
if mibBuilder.loadTexts: adNapClientIp.setDescription('NAP clients IP address.')
adNapClientHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientHostname.setStatus('current')
if mibBuilder.loadTexts: adNapClientHostname.setDescription('NAP clients hostname.')
adNapClientSrcPortIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientSrcPortIfId.setStatus('current')
if mibBuilder.loadTexts: adNapClientSrcPortIfId.setDescription('NAP clients source port interface ID.')
adNapClientSrcPortIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientSrcPortIfType.setStatus('current')
if mibBuilder.loadTexts: adNapClientSrcPortIfType.setDescription('NAP clients source port interface type.')
adNapServerMac = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapServerMac.setStatus('current')
if mibBuilder.loadTexts: adNapServerMac.setDescription('NAP servers MAC address.')
adNapServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapServerIp.setStatus('current')
if mibBuilder.loadTexts: adNapServerIp.setDescription('NAP servers IP address.')
adNapCollectionMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapCollectionMethod.setStatus('current')
if mibBuilder.loadTexts: adNapCollectionMethod.setDescription('Method by which the NAP information is collected.')
adNapCollectionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapCollectionTime.setStatus('current')
if mibBuilder.loadTexts: adNapCollectionTime.setDescription('Time when the NAP information was collected.')
adNapCapableClient = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapCapableClient.setStatus('current')
if mibBuilder.loadTexts: adNapCapableClient.setDescription('Client is NAP capable.')
adNapCapableServer = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapCapableServer.setStatus('current')
if mibBuilder.loadTexts: adNapCapableServer.setDescription('Server is NAP capable.')
adNapClientOsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientOsVersion.setStatus('current')
if mibBuilder.loadTexts: adNapClientOsVersion.setDescription('NAP clients OS version.')
adNapClientOsServicePk = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientOsServicePk.setStatus('current')
if mibBuilder.loadTexts: adNapClientOsServicePk.setDescription('NAP clients service pack.')
adNapClientOsProcessorArc = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientOsProcessorArc.setStatus('current')
if mibBuilder.loadTexts: adNapClientOsProcessorArc.setDescription('NAP clients processor architecture.')
adNapClientLastSecurityUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientLastSecurityUpdate.setStatus('current')
if mibBuilder.loadTexts: adNapClientLastSecurityUpdate.setDescription('Last time the NAP clients security was updated.')
adNapClientSecurityUpdateServer = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientSecurityUpdateServer.setStatus('current')
if mibBuilder.loadTexts: adNapClientSecurityUpdateServer.setDescription('NAP clients security update server.')
adNapClientRequiresRemediation = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("true", 2), ("false", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientRequiresRemediation.setStatus('current')
if mibBuilder.loadTexts: adNapClientRequiresRemediation.setDescription('NAP clients requires remediation.')
adNapClientLocalPolicyViolator = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientLocalPolicyViolator.setStatus('current')
if mibBuilder.loadTexts: adNapClientLocalPolicyViolator.setDescription('NAP clients violates local policies.')
adNapClientFirewallState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("unknown", 1), ("notInstalled", 2), ("wscServiceDown", 3), ("wscNotStarted", 4), ("notEnaNotUTD", 5), ("micsftNotEnaNotUTD", 6), ("notEnaUTD", 7), ("micsftNotEnaUTD", 8), ("enaNotUTDSn", 9), ("micsftEnaNotUTDSn", 10), ("enaNotUTDNotSn", 11), ("micsftEnaNotUTDNotSn", 12), ("enaUTDSn", 13), ("micsftEnaUTDSn", 14), ("enaUTDNotSn", 15), ("micsftEnaUTDNotSn", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientFirewallState.setStatus('current')
if mibBuilder.loadTexts: adNapClientFirewallState.setDescription('NAP clients firewall state.')
adNapClientFirewall = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientFirewall.setStatus('current')
if mibBuilder.loadTexts: adNapClientFirewall.setDescription('NAP clients firewall.')
adNapClientAntivirusState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("unknown", 1), ("notInstalled", 2), ("wscServiceDown", 3), ("wscNotStarted", 4), ("notEnaNotUTD", 5), ("micsftNotEnaNotUTD", 6), ("notEnaUTD", 7), ("micsftNotEnaUTD", 8), ("enaNotUTDSn", 9), ("micsftEnaNotUTDSn", 10), ("enaNotUTDNotSn", 11), ("micsftEnaNotUTDNotSn", 12), ("enaUTDSn", 13), ("micsftEnaUTDSn", 14), ("enaUTDNotSn", 15), ("micsftEnaUTDNotSn", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientAntivirusState.setStatus('current')
if mibBuilder.loadTexts: adNapClientAntivirusState.setDescription('NAP clients antivirus state.')
adNapClientAntivirus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientAntivirus.setStatus('current')
if mibBuilder.loadTexts: adNapClientAntivirus.setDescription('NAP clients antivirus.')
adNapClientAntispywareState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("unknown", 1), ("notInstalled", 2), ("wscServiceDown", 3), ("wscNotStarted", 4), ("notEnaNotUTD", 5), ("micsftNotEnaNotUTD", 6), ("notEnaUTD", 7), ("micsftNotEnaUTD", 8), ("enaNotUTDSn", 9), ("micsftEnaNotUTDSn", 10), ("enaNotUTDNotSn", 11), ("micsftEnaNotUTDNotSn", 12), ("enaUTDSn", 13), ("micsftEnaUTDSn", 14), ("enaUTDNotSn", 15), ("micsftEnaUTDNotSn", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientAntispywareState.setStatus('current')
if mibBuilder.loadTexts: adNapClientAntispywareState.setDescription('NAP clients antispyware state.')
adNapClientAntispyware = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientAntispyware.setStatus('current')
if mibBuilder.loadTexts: adNapClientAntispyware.setDescription('NAP clients antispyware.')
adNapClientAutoupdateState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unknown", 1), ("notInstalled", 2), ("wscServiceDown", 3), ("wscNotStarted", 4), ("notEna", 5), ("enaCkUpdateOnly", 6), ("enaDownload", 7), ("enaDownloadInstall", 8), ("neverConfigured", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientAutoupdateState.setStatus('current')
if mibBuilder.loadTexts: adNapClientAutoupdateState.setDescription('NAP clients auto update state.')
adNapClientSecurityupdateState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unknown", 1), ("noMissingUpdate", 2), ("missingUpdate", 3), ("noWUS", 4), ("noClientID", 5), ("wuaServiceDisabled", 6), ("wuaCommFailed", 7), ("updateInsNeedReboot", 8), ("wuaNotStarted", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientSecurityupdateState.setStatus('current')
if mibBuilder.loadTexts: adNapClientSecurityupdateState.setDescription('NAP clients security update state.')
adNapClientSecuritySeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("unspecified", 2), ("low", 3), ("moderate", 4), ("important", 5), ("critical", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientSecuritySeverity.setStatus('current')
if mibBuilder.loadTexts: adNapClientSecuritySeverity.setDescription('NAP clients security update severity.')
adNapClientConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("notRestricted", 2), ("notResMaybeLater", 3), ("restricted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientConnectionState.setStatus('current')
if mibBuilder.loadTexts: adNapClientConnectionState.setDescription('NAP clients network connection state.')
adGenAOSDesktopAuditingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10))
adGenAOSDesktopAuditingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1))
adGenAOSDesktopAuditingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 2))
adGenAOSDesktopAuditingFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 2, 1)).setObjects(("ADTRAN-AOS-DESKTOP-AUDITING", "adGenNapClientsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDesktopAuditingFullCompliance = adGenAOSDesktopAuditingFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOSDesktopAuditingFullCompliance.setDescription('The compliance statement for SNMP entities which implement\n        version 1 of the adGenAosDesktopAuditing MIB. When this MIB is implemented\n        with support for read-only, then such an implementation can claim\n        full compliance. ')
adGenNapClientsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 1)).setObjects(("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientMac"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientVlanId"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientIp"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientHostname"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSrcPortIfId"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSrcPortIfType"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapServerMac"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapServerIp"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCollectionMethod"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCollectionTime"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCapableClient"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCapableServer"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientOsVersion"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientOsServicePk"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientOsProcessorArc"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientLastSecurityUpdate"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSecurityUpdateServer"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientRequiresRemediation"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientLocalPolicyViolator"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientFirewallState"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientFirewall"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntivirusState"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntivirus"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntispywareState"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntispyware"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAutoupdateState"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSecurityupdateState"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSecuritySeverity"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientConnectionState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenNapClientsGroup = adGenNapClientsGroup.setStatus('current')
if mibBuilder.loadTexts: adGenNapClientsGroup.setDescription('The adGenNapClientGroup group contains read-only NAP information of clients\n            in the network that are NAP capable.')
mibBuilder.exportSymbols("ADTRAN-AOS-DESKTOP-AUDITING", adGenAOSDesktopAuditingFullCompliance=adGenAOSDesktopAuditingFullCompliance, adNapServerIp=adNapServerIp, adNapCapableServer=adNapCapableServer, adNapClientVlanId=adNapClientVlanId, adNapClientHostname=adNapClientHostname, adNapClientOsProcessorArc=adNapClientOsProcessorArc, adGenAOSDesktopAuditingConformance=adGenAOSDesktopAuditingConformance, adNapClientAntivirus=adNapClientAntivirus, adGenNapClientsGroup=adGenNapClientsGroup, adNapClientSrcPortIfType=adNapClientSrcPortIfType, adNapClientAntivirusState=adNapClientAntivirusState, adNapClientAntispywareState=adNapClientAntispywareState, adGenNapClients=adGenNapClients, adNapClientAutoupdateState=adNapClientAutoupdateState, adNapServerMac=adNapServerMac, adNapClientConnectionState=adNapClientConnectionState, adNapClientOsServicePk=adNapClientOsServicePk, adNapClientSecurityupdateState=adNapClientSecurityupdateState, adGenAOSDesktopAuditingMib=adGenAOSDesktopAuditingMib, adGenNapClientsTable=adGenNapClientsTable, adNapClientSecuritySeverity=adNapClientSecuritySeverity, adGenAOSDesktopAuditingGroups=adGenAOSDesktopAuditingGroups, adNapClientLocalPolicyViolator=adNapClientLocalPolicyViolator, adNapClientOsVersion=adNapClientOsVersion, adNapClientMac=adNapClientMac, adNapClientSrcPortIfId=adNapClientSrcPortIfId, adNapClientIp=adNapClientIp, adNapClientLastSecurityUpdate=adNapClientLastSecurityUpdate, adNapClientRequiresRemediation=adNapClientRequiresRemediation, adGenAOSDesktopAuditingCompliances=adGenAOSDesktopAuditingCompliances, adGenNapClientsEntry=adGenNapClientsEntry, adNapClientFirewallState=adNapClientFirewallState, adNapClientFirewall=adNapClientFirewall, PYSNMP_MODULE_ID=adGenAOSDesktopAuditingMib, adGenDesktopAuditing=adGenDesktopAuditing, adNapCapableClient=adNapCapableClient, adNapCollectionTime=adNapCollectionTime, adNapClientSecurityUpdateServer=adNapClientSecurityUpdateServer, adNapCollectionMethod=adNapCollectionMethod, adNapClientAntispyware=adNapClientAntispyware)
