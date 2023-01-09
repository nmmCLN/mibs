#
# PySNMP MIB module EQLINTERNAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLINTERNAL-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:49 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
UTFString, = mibBuilder.importSymbols("EQLGROUP-MIB", "UTFString")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, Bits, ModuleIdentity, MibIdentifier, Counter64, NotificationType, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, ObjectIdentity, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Bits", "ModuleIdentity", "MibIdentifier", "Counter64", "NotificationType", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "ObjectIdentity", "IpAddress", "TimeTicks")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
eqlInternalModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 27))
eqlInternalModule.setRevisions(('2013-01-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eqlInternalModule.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: eqlInternalModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlInternalModule.setOrganization('Dell Inc.')
if mibBuilder.loadTexts: eqlInternalModule.setContactInfo('Contact: Customer Support\n         Postal:  Dell Inc\n                  300 Innovative Way, Suite 301, Nashua, NH 03062\n         Tel:     +1 603-579-9762             \n         E-mail:  US-NH-CS-TechnicalSupport@dell.com\n         WEB:     www.equallogic.com')
if mibBuilder.loadTexts: eqlInternalModule.setDescription('Dell Inc Storage Array internal information to track monitoring and\n         licensing of group.\n\n         Copyright (c) 2003-2013 by Dell Inc.\n\n         All rights reserved.  This software may not be copied, disclosed,\n         transferred, or used except in accordance with a license granted\n         by Dell Inc.  This software embodies proprietary information\n         and trade secrets of Dell Inc.\n        ')
eqlInternalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 27, 1))
eqlMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1), )
if mibBuilder.loadTexts: eqlMonitorTable.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorTable.setDescription('EqualLogic-Persistent Monitor Table')
eqlMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1), ).setIndexNames((0, "EQLINTERNAL-MIB", "eqlMonitorIndex"))
if mibBuilder.loadTexts: eqlMonitorEntry.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorEntry.setDescription('An entry (row) containing information about hosts monitoring the group.')
eqlMonitorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlMonitorIndex.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorIndex.setDescription('This field specifies a unique index which identifies an monitoring instance.\n                     This field is a hash of the GUID.')
eqlMonitorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorRowStatus.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorRowStatus.setDescription('The status of the row')
eqlMonitorUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorUUID.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorUUID.setDescription('This field is for internal use only.')
eqlMonitorServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 4), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorServerName.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorServerName.setDescription('This field specifies the DNS server name of the host running SANHQ monitoring the group.\n                     Together with eqlSANHQDomainName it must be a name which is resolvable by DNS. There is no default for SANHQDNSName.')
eqlMonitorDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 5), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorDomainName.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorDomainName.setDescription('This field specifies the DNS domain name of the host running SANHQ monitoring the group.')
eqlMonitorInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 6), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorInetAddressType.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorInetAddressType.setDescription('The ip address type of the host monitoring this group.')
eqlMonitorInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorInetAddress.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorInetAddress.setDescription('The ip address, in network byte order, of the host monitoring this group.')
eqlMonitorSupportAssist = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("supportAssistNone", 0), ("supportAssistInstalledNotEnabled", 1), ("supportAssistEnabled", 2), ("supportAssistCommunicatingWithDell", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorSupportAssist.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorSupportAssist.setDescription('This field specifies how SupportAssist is currently monitoring this group.')
eqlMonitorTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 9), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorTimestamp.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorTimestamp.setDescription('This field specifies the last access time for SANHQ Monitoring.\n                     Time is represented as the time in seconds since 00:00:00 UTC, 1970-01-01.')
eqlMonitorSupportAssistTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 10), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorSupportAssistTimestamp.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorSupportAssistTimestamp.setDescription('This field specifies the last access time for SupportAssist.\n                     Time is represented as the time in seconds since 00:00:00 UTC, 1970-01-01.')
eqlMonitorLicensingTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 11), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorLicensingTimestamp.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorLicensingTimestamp.setDescription('This field specifies the last time SupportAssist sent licensing records to Dell.\n                     Time is represented as the time in seconds since 00:00:00 UTC, 1970-01-01.')
eqlMonitorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 12), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorDescription.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorDescription.setDescription('This field specifies a descriptive string that provides details about group monitoring.\n                     The description can be 128 octets. There is no default value.')
eqlMonitorStatusTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 27, 1, 2), )
if mibBuilder.loadTexts: eqlMonitorStatusTable.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorStatusTable.setDescription('EqualLogic-Dynamic Monitor Status Table')
eqlMonitorStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 27, 1, 2, 1), ).setIndexNames((0, "EQLINTERNAL-MIB", "eqlMonitorIndex"))
if mibBuilder.loadTexts: eqlMonitorStatusEntry.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorStatusEntry.setDescription('An entry (row) containing status information about hosts monitoring the group.')
eqlMonitorStatusReminder = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("monitoringExpired", 0), ("monitoringCurrent", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlMonitorStatusReminder.setStatus('current')
if mibBuilder.loadTexts: eqlMonitorStatusReminder.setDescription('This field indicates if the SANHQ currently monitoring this group\n                     has recently contacted the group.')
mibBuilder.exportSymbols("EQLINTERNAL-MIB", eqlInternalModule=eqlInternalModule, eqlMonitorTimestamp=eqlMonitorTimestamp, eqlMonitorDescription=eqlMonitorDescription, eqlMonitorUUID=eqlMonitorUUID, eqlMonitorStatusEntry=eqlMonitorStatusEntry, eqlMonitorSupportAssist=eqlMonitorSupportAssist, eqlMonitorServerName=eqlMonitorServerName, eqlMonitorTable=eqlMonitorTable, PYSNMP_MODULE_ID=eqlInternalModule, eqlMonitorStatusTable=eqlMonitorStatusTable, eqlInternalObjects=eqlInternalObjects, eqlMonitorIndex=eqlMonitorIndex, eqlMonitorEntry=eqlMonitorEntry, eqlMonitorDomainName=eqlMonitorDomainName, eqlMonitorRowStatus=eqlMonitorRowStatus, eqlMonitorSupportAssistTimestamp=eqlMonitorSupportAssistTimestamp, eqlMonitorInetAddress=eqlMonitorInetAddress, eqlMonitorLicensingTimestamp=eqlMonitorLicensingTimestamp, eqlMonitorStatusReminder=eqlMonitorStatusReminder, eqlMonitorInetAddressType=eqlMonitorInetAddressType)
