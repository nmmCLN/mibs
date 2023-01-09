#
# PySNMP MIB module SL-OPT-APS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-OPT-APS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:40 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
slmTrapLogId, = mibBuilder.importSymbols("SL-MAIN-MIB", "slmTrapLogId")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, ObjectIdentity, Gauge32, MibIdentifier, TimeTicks, iso, Counter64, Opaque, Counter32, ModuleIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Gauge32", "MibIdentifier", "TimeTicks", "iso", "Counter64", "Opaque", "Counter32", "ModuleIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
slOptApsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 11))
if mibBuilder.loadTexts: slOptApsMib.setLastUpdated('200201140000Z')
if mibBuilder.loadTexts: slOptApsMib.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slOptApsMib.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slOptApsMib.setDescription('This MIB module describes the Optical APS.')
slOptApsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1))
slOptApsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2))
slOptApsTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 0))
optApsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1), )
if mibBuilder.loadTexts: optApsConfigTable.setStatus('current')
if mibBuilder.loadTexts: optApsConfigTable.setDescription('This table contains objects to configure APS \n              (Automatic Protection Switching) feature in a Optical \n              Channel. APS is the ability to configure a pair of Optical \n              connections for redundancy so that the hardware will \n              automatically switch the active connection from working connection\n              to the protection connection or vice versa, within 50ms, \n              when the active connection fails.\n              The optical connections are specified in the \n              optXpdConnConfigTable in the SL-OPT-MIB.\n              The APS is defined be specifying two entries in this table\n              the backup each other.\n              The optXpdConnConfigTable defines two entries for each dircetion\n              of the connection.\n              Only one of the two entries is used by the optical aps table.\n              The direction that is used is the direction from the User to Network.')
optApsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1), ).setIndexNames((0, "SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"))
if mibBuilder.loadTexts: optApsConfigEntry.setStatus('current')
if mibBuilder.loadTexts: optApsConfigEntry.setDescription('An entry is identified by two transponding connections\n            that should protect each other.')
optApsConfigUserWorkingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigUserWorkingIndex.setStatus('current')
if mibBuilder.loadTexts: optApsConfigUserWorkingIndex.setDescription('The ifIndex of the working optical interface connected to\n         the User side.')
optApsConfigNetWorkingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigNetWorkingIndex.setStatus('current')
if mibBuilder.loadTexts: optApsConfigNetWorkingIndex.setDescription('The ifIndex of the working optical interface connected to\n         the Network side.')
optApsConfigUserProtectingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigUserProtectingIndex.setStatus('current')
if mibBuilder.loadTexts: optApsConfigUserProtectingIndex.setDescription('The ifIndex of the protecting optical interface connected to\n         the User side. In the case of an Inline connection there is no\n         meaning to the order between the User and Network interfaces because\n         both side of the connections are connected to the Network.')
optApsConfigNetProtectingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigNetProtectingIndex.setStatus('current')
if mibBuilder.loadTexts: optApsConfigNetProtectingIndex.setDescription('The ifIndex of the protecting optical interface connected to\n         the Network side. In the case of an Inline connection there is no\n         meaning to the order between the User and Network interfaces because\n         both side of the connections are connected to the Network.')
optApsConfigScheme = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equipment", 1), ("facility", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigScheme.setStatus('current')
if mibBuilder.loadTexts: optApsConfigScheme.setDescription("This object is used to configure the optical \n      \tprotection scheme. \n\n      \tequipment : Equipmet protection (with 4 FEO's)\n      \tfacility  : Facility protection (only 3 FEO's)")
optApsConfigEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("optApsDisabled", 1), ("optApsEnabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigEnable.setStatus('current')
if mibBuilder.loadTexts: optApsConfigEnable.setDescription('This object is used to enable or disable the APS feature\n           on the working/protection connection pairs. When enabled,\n           the hardware will automatically switch the active connection \n           from the working connection to the protection connection within 50ms,\n           or vice versa (read-write).')
optApsConfigArchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("onePlusOne", 1), ("oneToOne", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigArchMode.setStatus('current')
if mibBuilder.loadTexts: optApsConfigArchMode.setDescription('This object is used to configure APS architecture mode\n         on the working/protection connection pairs (read-write).')
optApsConfigActiveConnectionRx = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("optApsWorkingConnection", 1), ("optApsProtectionConnection", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigActiveConnectionRx.setStatus('current')
if mibBuilder.loadTexts: optApsConfigActiveConnectionRx.setDescription('This object indicates which Rx connection is currently active. \n            It could be the working connection, the protection connection or \n            none if neither working nor protection connection is active. \n            This object reflects the status of receive direction.\n            If optApsDirection is equal to biDirectional this object should\n            be eual to optApsActiveConnectionRx.')
optApsConfigActiveConnectionTx = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("optApsWorkingConnection", 1), ("optApsProtectionConnection", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigActiveConnectionTx.setStatus('current')
if mibBuilder.loadTexts: optApsConfigActiveConnectionTx.setDescription('This object indicates which Tx connection is currently active. \n            It could be the working connection, the protection connection or \n            none if neither working nor protection connection is active. \n            This object reflects the status of receive direction.\n            If optApsDirection is equal to biDirectional this object should\n            be eual to optApsActiveConnectionRx.')
optApsConfigWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigWaitToRestore.setStatus('current')
if mibBuilder.loadTexts: optApsConfigWaitToRestore.setDescription("This object contains interval in minutes to wait \n                 before attempting to switch back to working connection. \n                 Not applicable if the connection is configured in \n                 non-revertive mode, i.e. protection connection will \n                 continue to be active, even if failures on the \n                 working connection are cleared. The framer clears the \n                 signal-fault and signal-degrade when APS switch \n                 occurs. Please refer to 'optApsRevertive' for \n                 description of non-revertive (read-write).")
optApsConfigDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uniDirectional", 1), ("biDirectional", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigDirection.setStatus('current')
if mibBuilder.loadTexts: optApsConfigDirection.setDescription('This object is used to configure the switching \n               direction which this APS connection supports (read-write). \n\n               Unidirectional : APS switch only in one direction.\n               Bidirectional  : APS switch in both ends of the conection.')
optApsConfigRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nonrevertive", 1), ("revertive", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigRevertive.setStatus('current')
if mibBuilder.loadTexts: optApsConfigRevertive.setDescription("This object is used to configure the APS revertive or\n            nonrevertive option (read-write). \n    \n            revertive : \n              Will switch the working connection back to active state after\n              the Wait-To-restore interval has expired and the \n              working connection Signal-Fault/Signal-Degrade has been \n              cleared. Please refer to 'optApsWaitToRestore' for \n              description of Wait-To-Restore interval.\n            nonrevertive : \n              The  protection connection continues to be the active connection,\n              The active connection does not switch to the working connection.")
optApsConfigChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 13), Bits().clone(namedValues=NamedValues(("lockedOut", 0), ("sfWorking", 1), ("sfProtecting", 2), ("switched", 3), ("lockedOutRemote", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigChanStatus.setStatus('current')
if mibBuilder.loadTexts: optApsConfigChanStatus.setDescription('Indicates the current state of the port.\n\n            lockedOut\n            This bit, when applied to a working channel, indicates that\n            the channel is prevented from switching to the protection connection.\n            When applied to the null channel, this bit indicates that no\n            working channel may switch to the protection connection.\n\n            sfWorking\n            A signal failure condition on the working connection is in effect.\n\n            sfProtecting\n            A signal failure condition on the protecting connection is in effect.\n\n            switched\n            The switched bit is applied to a working channel if that\n            channel is currently switched to the protection connection.\n            \n\t\t\tlockedOutRemote\n\t\t\tIndicate that the protection is locked out by \n            command issued on the remote NE.')
optApsConfigChanSignalFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigChanSignalFailures.setStatus('current')
if mibBuilder.loadTexts: optApsConfigChanSignalFailures.setDescription('A count of Signal Failure conditions that have been\n            detected on the incoming signal. This condition occurs\n            when a loss of signal is detected.')
optApsConfigChanSwitchovers = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigChanSwitchovers.setStatus('current')
if mibBuilder.loadTexts: optApsConfigChanSwitchovers.setDescription('The number of times this channel has switched to the protection\n            connection. When queried with index value apsChanNumber set to 0, which\n            is the protection connection, this object will return 0. ')
optApsConfigChanLastSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 16), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigChanLastSwitchover.setStatus('current')
if mibBuilder.loadTexts: optApsConfigChanLastSwitchover.setDescription('The value of sysUpTime when this channel last completed a switch\n            to the protection connection. If this channel has never switched to the\n            protection connection, or this channel is the protection connection, the value\n            0  will be returned.')
optApsConfigSwitchCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("clear", 1), ("lockoutOfProtection", 2), ("forcedSwitchOfWorking", 3), ("forcedSwitchOfProtection", 4), ("manualSwitchOfWorking", 5), ("manualSwitchOfProtection", 6))).clone('clear')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigSwitchCommand.setStatus('current')
if mibBuilder.loadTexts: optApsConfigSwitchCommand.setDescription('A switch command initiates one external request for evaluation\n        (read-write).\n\n        (1) Clear - Clears all switch commands on the channel.\n\n        (2) Lockout Of Protection - Prevents any of the working channels\n        from switching to the protection connection by issuing a Lockout of\n        Protection request [unless a request of equal priority (i.e., a\n        Lockout of Protection) is already in effect].\n\n        (3) Forced Switch of Working (to Protection) - Switches the\n        working channel to the protection connection unless a request of equal\n        or higher priority is in effect, by issuing a Forced Switch\n        request.\n\n        (4) Forced Switch of Protection (to Working) - Switches the\n        working channel back from the protection connection to the working\n        connection unless a request of equal or higher priority is in effect,\n        by issuing a Forced Switch request.  This command applies only\n        in the 1+1 architecture.\n\n        (5) Manual Switch of Working (to Protection) - Switches the\n        working channel to the protection connection unless a request of equal\n        or higher priority is in effect, by issuing a Manual Switch\n        request.\n\n        (6) Manual Switch of Protection (to Working) - Switches the\n        working channel back from the protection connection to the working\n        connection unless a request of equal or higher priority is in effect,\n        by issuing a Manual Switch request.  This command applies only\n        in the 1+1 architecture for the null.\n\n        Reading this variable always returns zero (0).')
optApsConfigSwitchReason = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("optApsOther", 1), ("optApsRevertive", 2), ("optApsManual", 3), ("optApsSignalFailure", 4), ("optApsForceSwitch", 5), ("optApsLockOut", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigSwitchReason.setStatus('current')
if mibBuilder.loadTexts: optApsConfigSwitchReason.setDescription('The reason why APS switch happened. When the working\n           connection on one end fails, its other end is told to do\n           an  APS switch. The following options in the increasing\n           order of priority indicate what type of switch request \n           it is. \n\n          optApsRevertive : Switch back to working connection after the \n            Wait-to-Restore interval is over, and failures are \n            cleared. It is the lowest priority.\n          optApsManual : Manual switch causes APS switch unless a \n            request of equal or higher priority is in effect.\n          optApsSignalFailureHigh : switch occured due to SD failure. \n          optApsForceSwitch : Forced switch forces hardware to switch\n            the active connection even if the other connection (could be \n            working connection or protection connection) is in alarm.\n          optApsLockOut : This is the highest priority switch. This\n            will override all other requests. \n          optApsLockOut :  indicates that the last switchover to the \n            working occurred because of protection lockout.')
optApsConfigResetCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCounters", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigResetCounters.setStatus('current')
if mibBuilder.loadTexts: optApsConfigResetCounters.setDescription('Setting this variable to 1 will cause the counters\n        on all of the Optical APS Config Table to be initialized \n        to zero (read-write).')
optApsConfigActiveRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("optApsOther", 1), ("optApsRevertive", 2), ("optApsManual", 3), ("optApsSignalFailure", 4), ("optApsForceSwitch", 5), ("optApsLockOut", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optApsConfigActiveRequest.setStatus('current')
if mibBuilder.loadTexts: optApsConfigActiveRequest.setDescription('The Active Switch APS request:\n\n          optApsRevertive : Switch back to working connection after the \n            Wait-to-Restore interval is over, and failures are \n            cleared. It is the lowest priority.\n          optApsManual : Manual switch causes APS switch unless a \n            request of equal or higher priority is in effect.\n          optApsSignalFailure : Switch due to signal failure.\n          optApsForceSwitch : Forced switch forces hardware to switch\n            the active connection even if the other connection (could be \n            working connection or protection connection) is in alarm.\n          optApsLockOut : This is the highest priority switch. This\n            will override all other requests. \n          optApsLockOut :  indicates that the last switchover to the \n            working occurred because of protection lockout.')
optApsConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 21), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: optApsConfigStatus.setStatus('current')
if mibBuilder.loadTexts: optApsConfigStatus.setDescription('This object is used to create and delete rows in the\n               optApsConfigTable.')
optApsConfigLosThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optApsConfigLosThreshold.setStatus('current')
if mibBuilder.loadTexts: optApsConfigLosThreshold.setDescription('Configured threshold value for LOS detection of the optical switch.\n\t\tThis object is applicable only when slmOpticalSwitchExist is TRUE. \n\t\tThe value given in 0.1 dBm units. The range starts with -50.0 dBm.')
eqptApsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2), )
if mibBuilder.loadTexts: eqptApsConfigTable.setStatus('current')
if mibBuilder.loadTexts: eqptApsConfigTable.setDescription('This table contains objects to configure Equipment APS \n              (Automatic Protection Switching) feature.')
eqptApsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1), ).setIndexNames((0, "SL-OPT-APS-MIB", "eqptApsConfigDummyIndex"))
if mibBuilder.loadTexts: eqptApsConfigEntry.setStatus('current')
if mibBuilder.loadTexts: eqptApsConfigEntry.setDescription('This configuration is on device level thus only one entry exists.')
eqptApsConfigDummyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqptApsConfigDummyIndex.setStatus('current')
if mibBuilder.loadTexts: eqptApsConfigDummyIndex.setDescription('A dummy index. Always 1.')
eqptApsConfigRole = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("eqptApsWorkingRole", 1), ("eqptApsProtectionRole", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqptApsConfigRole.setStatus('current')
if mibBuilder.loadTexts: eqptApsConfigRole.setDescription('The device role.')
eqptApsConfigMate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqptApsConfigMate.setStatus('current')
if mibBuilder.loadTexts: eqptApsConfigMate.setDescription('The IP address of the mate device.')
eqptApsConfigLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("eqptApsLinkUp", 1), ("eqptApsLinkDown", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqptApsConfigLinkStatus.setStatus('current')
if mibBuilder.loadTexts: eqptApsConfigLinkStatus.setDescription('The IP address of the mate device.')
optApsTrapSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 1)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"), ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"))
if mibBuilder.loadTexts: optApsTrapSwitchover.setStatus('current')
if mibBuilder.loadTexts: optApsTrapSwitchover.setDescription('An optApsTrapSwitchover notification is sent when the\n               value of an instance of optApsChanSwitchovers increments.')
optApsConfigTableChanged = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 2)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"))
if mibBuilder.loadTexts: optApsConfigTableChanged.setStatus('current')
if mibBuilder.loadTexts: optApsConfigTableChanged.setDescription('An optApsConfigTableChanged notification is sent when the\n               content of the optApsConfigTable is changed.\n               The added/deleted entry is identified by the\n               optApsUserWorkingIndex object.')
optApsTrapSwitchover0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 0, 1)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"), ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"), ("SL-MAIN-MIB", "slmTrapLogId"))
if mibBuilder.loadTexts: optApsTrapSwitchover0.setStatus('current')
if mibBuilder.loadTexts: optApsTrapSwitchover0.setDescription("An optApsTrapSwitchover notification is sent when the\n               value of an instance of optApsChanSwitchovers increments.\n               It is defined to support browsers that don't recognize RFC 2576.")
optApsConfigTableChanged0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 0, 2)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"), ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"), ("SL-MAIN-MIB", "slmTrapLogId"))
if mibBuilder.loadTexts: optApsConfigTableChanged0.setStatus('current')
if mibBuilder.loadTexts: optApsConfigTableChanged0.setDescription("An optApsConfigTableChanged notification is sent when the\n               content of the optApsConfigTable is changed.\n               The added/deleted entry is identified by the\n               optApsUserWorkingIndex object.\n               It is defined to support browsers that don't recognize RFC 2576.")
mibBuilder.exportSymbols("SL-OPT-APS-MIB", optApsConfigTable=optApsConfigTable, optApsConfigTableChanged0=optApsConfigTableChanged0, eqptApsConfigLinkStatus=eqptApsConfigLinkStatus, optApsTrapSwitchover0=optApsTrapSwitchover0, optApsConfigUserProtectingIndex=optApsConfigUserProtectingIndex, optApsConfigTableChanged=optApsConfigTableChanged, optApsConfigUserWorkingIndex=optApsConfigUserWorkingIndex, optApsConfigActiveConnectionRx=optApsConfigActiveConnectionRx, optApsConfigResetCounters=optApsConfigResetCounters, optApsConfigNetWorkingIndex=optApsConfigNetWorkingIndex, optApsConfigWaitToRestore=optApsConfigWaitToRestore, optApsConfigChanLastSwitchover=optApsConfigChanLastSwitchover, optApsConfigEnable=optApsConfigEnable, optApsConfigSwitchReason=optApsConfigSwitchReason, optApsConfigChanStatus=optApsConfigChanStatus, optApsConfigActiveRequest=optApsConfigActiveRequest, eqptApsConfigDummyIndex=eqptApsConfigDummyIndex, optApsTrapSwitchover=optApsTrapSwitchover, slOptApsConfig=slOptApsConfig, optApsConfigDirection=optApsConfigDirection, optApsConfigStatus=optApsConfigStatus, optApsConfigChanSwitchovers=optApsConfigChanSwitchovers, slOptApsTraps=slOptApsTraps, optApsConfigLosThreshold=optApsConfigLosThreshold, optApsConfigChanSignalFailures=optApsConfigChanSignalFailures, optApsConfigActiveConnectionTx=optApsConfigActiveConnectionTx, eqptApsConfigRole=eqptApsConfigRole, PYSNMP_MODULE_ID=slOptApsMib, eqptApsConfigTable=eqptApsConfigTable, optApsConfigArchMode=optApsConfigArchMode, optApsConfigRevertive=optApsConfigRevertive, optApsConfigScheme=optApsConfigScheme, optApsConfigSwitchCommand=optApsConfigSwitchCommand, optApsConfigEntry=optApsConfigEntry, optApsConfigNetProtectingIndex=optApsConfigNetProtectingIndex, eqptApsConfigMate=eqptApsConfigMate, slOptApsMib=slOptApsMib, slOptApsTraps0=slOptApsTraps0, eqptApsConfigEntry=eqptApsConfigEntry)
