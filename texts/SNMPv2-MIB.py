#
# PySNMP MIB module SNMPv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:20 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, NotificationType, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Bits, ObjectIdentity, Unsigned32, TimeTicks, Counter32, mib_2, IpAddress, snmpModules, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Bits", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter32", "mib-2", "IpAddress", "snmpModules", "iso")
TimeStamp, TestAndIncr, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TestAndIncr", "DisplayString", "TextualConvention")
snmpMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 1))
snmpMIB.setRevisions(('2002-10-16 00:00', '1995-11-09 00:00', '1993-04-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpMIB.setRevisionsDescriptions(('This revision of this MIB module was published as\n             RFC 3418.', 'This revision of this MIB module was published as\n             RFC 1907.', 'The initial revision of this MIB module was published\n            as RFC 1450.',))
if mibBuilder.loadTexts: snmpMIB.setLastUpdated('200210160000Z')
if mibBuilder.loadTexts: snmpMIB.setOrganization('IETF SNMPv3 Working Group')
if mibBuilder.loadTexts: snmpMIB.setContactInfo('WG-EMail:   snmpv3@lists.tislabs.com\n             Subscribe:  snmpv3-request@lists.tislabs.com\n\n             Co-Chair:   Russ Mundy\n                         Network Associates Laboratories\n             postal:     15204 Omega Drive, Suite 300\n                         Rockville, MD 20850-4601\n                         USA\n             EMail:      mundy@tislabs.com\n             phone:      +1 301 947-7107\n\n             Co-Chair:   David Harrington\n                         Enterasys Networks\n             postal:     35 Industrial Way\n                         P. O. Box 5005\n                         Rochester, NH 03866-5005\n                         USA\n             EMail:      dbh@enterasys.com\n             phone:      +1 603 337-2614\n\n             Editor:     Randy Presuhn\n                         BMC Software, Inc.\n             postal:     2141 North First Street\n                         San Jose, CA 95131\n                         USA\n             EMail:      randy_presuhn@bmc.com\n             phone:      +1 408 546-1006')
if mibBuilder.loadTexts: snmpMIB.setDescription('The MIB module for SNMP entities.\n\n             Copyright (C) The Internet Society (2002). This\n             version of this MIB module is part of RFC 3418;\n             see the RFC itself for full legal notices.\n            ')
snmpMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1))
system = MibIdentifier((1, 3, 6, 1, 2, 1, 1))
sysDescr = MibScalar((1, 3, 6, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDescr.setStatus('current')
if mibBuilder.loadTexts: sysDescr.setDescription("A textual description of the entity.  This value should\n            include the full name and version identification of\n            the system's hardware type, software operating-system,\n            and networking software.")
sysObjectID = MibScalar((1, 3, 6, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysObjectID.setStatus('current')
if mibBuilder.loadTexts: sysObjectID.setDescription("The vendor's authoritative identification of the\n            network management subsystem contained in the entity.\n            This value is allocated within the SMI enterprises\n            subtree (1.3.6.1.4.1) and provides an easy and\n            unambiguous means for determining `what kind of box' is\n            being managed.  For example, if vendor `Flintstones,\n            Inc.' was assigned the subtree 1.3.6.1.4.1.424242,\n            it could assign the identifier 1.3.6.1.4.1.424242.1.1\n            to its `Fred Router'.")
sysUpTime = MibScalar((1, 3, 6, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUpTime.setStatus('current')
if mibBuilder.loadTexts: sysUpTime.setDescription('The time (in hundredths of a second) since the\n            network management portion of the system was last\n            re-initialized.')
sysContact = MibScalar((1, 3, 6, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysContact.setStatus('current')
if mibBuilder.loadTexts: sysContact.setDescription('The textual identification of the contact person for\n            this managed node, together with information on how\n            to contact this person.  If no contact information is\n            known, the value is the zero-length string.')
sysName = MibScalar((1, 3, 6, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysName.setStatus('current')
if mibBuilder.loadTexts: sysName.setDescription("An administratively-assigned name for this managed\n            node.  By convention, this is the node's fully-qualified\n            domain name.  If the name is unknown, the value is\n            the zero-length string.")
sysLocation = MibScalar((1, 3, 6, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysLocation.setStatus('current')
if mibBuilder.loadTexts: sysLocation.setDescription("The physical location of this node (e.g., 'telephone\n            closet, 3rd floor').  If the location is unknown, the\n            value is the zero-length string.")
sysServices = MibScalar((1, 3, 6, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysServices.setStatus('current')
if mibBuilder.loadTexts: sysServices.setDescription('A value which indicates the set of services that this\n            entity may potentially offer.  The value is a sum.\n\n\n\n            This sum initially takes the value zero. Then, for\n            each layer, L, in the range 1 through 7, that this node\n            performs transactions for, 2 raised to (L - 1) is added\n            to the sum.  For example, a node which performs only\n            routing functions would have a value of 4 (2^(3-1)).\n            In contrast, a node which is a host offering application\n            services would have a value of 72 (2^(4-1) + 2^(7-1)).\n            Note that in the context of the Internet suite of\n            protocols, values should be calculated accordingly:\n\n                 layer      functionality\n                   1        physical (e.g., repeaters)\n                   2        datalink/subnetwork (e.g., bridges)\n                   3        internet (e.g., supports the IP)\n                   4        end-to-end  (e.g., supports the TCP)\n                   7        applications (e.g., supports the SMTP)\n\n            For systems including OSI protocols, layers 5 and 6\n            may also be counted.')
sysORLastChange = MibScalar((1, 3, 6, 1, 2, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysORLastChange.setStatus('current')
if mibBuilder.loadTexts: sysORLastChange.setDescription('The value of sysUpTime at the time of the most recent\n            change in state or value of any instance of sysORID.')
sysORTable = MibTable((1, 3, 6, 1, 2, 1, 1, 9), )
if mibBuilder.loadTexts: sysORTable.setStatus('current')
if mibBuilder.loadTexts: sysORTable.setDescription('The (conceptual) table listing the capabilities of\n            the local SNMP application acting as a command\n            responder with respect to various MIB modules.\n            SNMP entities having dynamically-configurable support\n            of MIB modules will have a dynamically-varying number\n            of conceptual rows.')
sysOREntry = MibTableRow((1, 3, 6, 1, 2, 1, 1, 9, 1), ).setIndexNames((0, "SNMPv2-MIB", "sysORIndex"))
if mibBuilder.loadTexts: sysOREntry.setStatus('current')
if mibBuilder.loadTexts: sysOREntry.setDescription('An entry (conceptual row) in the sysORTable.')
sysORIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: sysORIndex.setStatus('current')
if mibBuilder.loadTexts: sysORIndex.setDescription('The auxiliary variable used for identifying instances\n            of the columnar objects in the sysORTable.')
sysORID = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysORID.setStatus('current')
if mibBuilder.loadTexts: sysORID.setDescription('An authoritative identification of a capabilities\n            statement with respect to various MIB modules supported\n            by the local SNMP application acting as a command\n            responder.')
sysORDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysORDescr.setStatus('current')
if mibBuilder.loadTexts: sysORDescr.setDescription('A textual description of the capabilities identified\n            by the corresponding instance of sysORID.')
sysORUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysORUpTime.setStatus('current')
if mibBuilder.loadTexts: sysORUpTime.setDescription('The value of sysUpTime at the time this conceptual\n            row was last instantiated.')
snmp = MibIdentifier((1, 3, 6, 1, 2, 1, 11))
snmpInPkts = MibScalar((1, 3, 6, 1, 2, 1, 11, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInPkts.setStatus('current')
if mibBuilder.loadTexts: snmpInPkts.setDescription('The total number of messages delivered to the SNMP\n            entity from the transport service.')
snmpInBadVersions = MibScalar((1, 3, 6, 1, 2, 1, 11, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInBadVersions.setStatus('current')
if mibBuilder.loadTexts: snmpInBadVersions.setDescription('The total number of SNMP messages which were delivered\n            to the SNMP entity and were for an unsupported SNMP\n            version.')
snmpInBadCommunityNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInBadCommunityNames.setStatus('current')
if mibBuilder.loadTexts: snmpInBadCommunityNames.setDescription('The total number of community-based SNMP messages (for\n           example,  SNMPv1) delivered to the SNMP entity which\n           used an SNMP community name not known to said entity.\n           Also, implementations which authenticate community-based\n           SNMP messages using check(s) in addition to matching\n           the community name (for example, by also checking\n           whether the message originated from a transport address\n           allowed to use a specified community name) MAY include\n           in this value the number of messages which failed the\n           additional check(s).  It is strongly RECOMMENDED that\n\n\n\n           the documentation for any security model which is used\n           to authenticate community-based SNMP messages specify\n           the precise conditions that contribute to this value.')
snmpInBadCommunityUses = MibScalar((1, 3, 6, 1, 2, 1, 11, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInBadCommunityUses.setStatus('current')
if mibBuilder.loadTexts: snmpInBadCommunityUses.setDescription('The total number of community-based SNMP messages (for\n           example, SNMPv1) delivered to the SNMP entity which\n           represented an SNMP operation that was not allowed for\n           the SNMP community named in the message.  The precise\n           conditions under which this counter is incremented\n           (if at all) depend on how the SNMP entity implements\n           its access control mechanism and how its applications\n           interact with that access control mechanism.  It is\n           strongly RECOMMENDED that the documentation for any\n           access control mechanism which is used to control access\n           to and visibility of MIB instrumentation specify the\n           precise conditions that contribute to this value.')
snmpInASNParseErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInASNParseErrs.setStatus('current')
if mibBuilder.loadTexts: snmpInASNParseErrs.setDescription('The total number of ASN.1 or BER errors encountered by\n            the SNMP entity when decoding received SNMP messages.')
snmpEnableAuthenTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpEnableAuthenTraps.setStatus('current')
if mibBuilder.loadTexts: snmpEnableAuthenTraps.setDescription('Indicates whether the SNMP entity is permitted to\n            generate authenticationFailure traps.  The value of this\n            object overrides any configuration information; as such,\n            it provides a means whereby all authenticationFailure\n            traps may be disabled.\n\n            Note that it is strongly recommended that this object\n            be stored in non-volatile memory so that it remains\n            constant across re-initializations of the network\n            management system.')
snmpSilentDrops = MibScalar((1, 3, 6, 1, 2, 1, 11, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpSilentDrops.setStatus('current')
if mibBuilder.loadTexts: snmpSilentDrops.setDescription('The total number of Confirmed Class PDUs (such as\n           GetRequest-PDUs, GetNextRequest-PDUs,\n           GetBulkRequest-PDUs, SetRequest-PDUs, and\n           InformRequest-PDUs) delivered to the SNMP entity which\n           were silently dropped because the size of a reply\n           containing an alternate Response Class PDU (such as a\n           Response-PDU) with an empty variable-bindings field\n           was greater than either a local constraint or the\n           maximum message size associated with the originator of\n           the request.')
snmpProxyDrops = MibScalar((1, 3, 6, 1, 2, 1, 11, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpProxyDrops.setStatus('current')
if mibBuilder.loadTexts: snmpProxyDrops.setDescription('The total number of Confirmed Class PDUs\n            (such as GetRequest-PDUs, GetNextRequest-PDUs,\n            GetBulkRequest-PDUs, SetRequest-PDUs, and\n            InformRequest-PDUs) delivered to the SNMP entity which\n            were silently dropped because the transmission of\n            the (possibly translated) message to a proxy target\n            failed in a manner (other than a time-out) such that\n            no Response Class PDU (such as a Response-PDU) could\n            be returned.')
snmpTrap = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1, 4))
snmpTrapOID = MibScalar((1, 3, 6, 1, 6, 3, 1, 1, 4, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: snmpTrapOID.setStatus('current')
if mibBuilder.loadTexts: snmpTrapOID.setDescription('The authoritative identification of the notification\n            currently being sent.  This variable occurs as\n            the second varbind in every SNMPv2-Trap-PDU and\n            InformRequest-PDU.')
snmpTrapEnterprise = MibScalar((1, 3, 6, 1, 6, 3, 1, 1, 4, 3), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: snmpTrapEnterprise.setStatus('current')
if mibBuilder.loadTexts: snmpTrapEnterprise.setDescription('The authoritative identification of the enterprise\n            associated with the trap currently being sent.  When an\n            SNMP proxy agent is mapping an RFC1157 Trap-PDU\n            into a SNMPv2-Trap-PDU, this variable occurs as the\n            last varbind.')
snmpTraps = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1, 5))
coldStart = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 1))
if mibBuilder.loadTexts: coldStart.setStatus('current')
if mibBuilder.loadTexts: coldStart.setDescription('A coldStart trap signifies that the SNMP entity,\n            supporting a notification originator application, is\n            reinitializing itself and that its configuration may\n            have been altered.')
warmStart = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 2))
if mibBuilder.loadTexts: warmStart.setStatus('current')
if mibBuilder.loadTexts: warmStart.setDescription('A warmStart trap signifies that the SNMP entity,\n            supporting a notification originator application,\n            is reinitializing itself such that its configuration\n            is unaltered.')
authenticationFailure = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 5))
if mibBuilder.loadTexts: authenticationFailure.setStatus('current')
if mibBuilder.loadTexts: authenticationFailure.setDescription('An authenticationFailure trap signifies that the SNMP\n             entity has received a protocol message that is not\n             properly authenticated.  While all implementations\n             of SNMP entities MAY be capable of generating this\n             trap, the snmpEnableAuthenTraps object indicates\n             whether this trap will be generated.')
snmpSet = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1, 6))
snmpSetSerialNo = MibScalar((1, 3, 6, 1, 6, 3, 1, 1, 6, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpSetSerialNo.setStatus('current')
if mibBuilder.loadTexts: snmpSetSerialNo.setDescription('An advisory lock used to allow several cooperating\n            command generator applications to coordinate their\n            use of the SNMP set operation.\n\n            This object is used for coarse-grain coordination.\n            To achieve fine-grain coordination, one or more similar\n            objects might be defined within each MIB group, as\n            appropriate.')
snmpMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 2))
snmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 2, 1))
snmpMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 2, 2))
snmpBasicCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 1, 2, 1, 2)).setObjects(("SNMPv2-MIB", "snmpGroup"), ("SNMPv2-MIB", "snmpSetGroup"), ("SNMPv2-MIB", "systemGroup"), ("SNMPv2-MIB", "snmpBasicNotificationsGroup"), ("SNMPv2-MIB", "snmpCommunityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpBasicCompliance = snmpBasicCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: snmpBasicCompliance.setDescription('The compliance statement for SNMPv2 entities which\n            implement the SNMPv2 MIB.\n\n            This compliance statement is replaced by\n            snmpBasicComplianceRev2.')
snmpBasicComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 6, 3, 1, 2, 1, 3)).setObjects(("SNMPv2-MIB", "snmpGroup"), ("SNMPv2-MIB", "snmpSetGroup"), ("SNMPv2-MIB", "systemGroup"), ("SNMPv2-MIB", "snmpBasicNotificationsGroup"), ("SNMPv2-MIB", "snmpCommunityGroup"), ("SNMPv2-MIB", "snmpWarmStartNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpBasicComplianceRev2 = snmpBasicComplianceRev2.setStatus('current')
if mibBuilder.loadTexts: snmpBasicComplianceRev2.setDescription('The compliance statement for SNMP entities which\n            implement this MIB module.')
snmpGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 8)).setObjects(("SNMPv2-MIB", "snmpInPkts"), ("SNMPv2-MIB", "snmpInBadVersions"), ("SNMPv2-MIB", "snmpInASNParseErrs"), ("SNMPv2-MIB", "snmpSilentDrops"), ("SNMPv2-MIB", "snmpProxyDrops"), ("SNMPv2-MIB", "snmpEnableAuthenTraps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpGroup = snmpGroup.setStatus('current')
if mibBuilder.loadTexts: snmpGroup.setDescription('A collection of objects providing basic instrumentation\n            and control of an SNMP entity.')
snmpCommunityGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 9)).setObjects(("SNMPv2-MIB", "snmpInBadCommunityNames"), ("SNMPv2-MIB", "snmpInBadCommunityUses"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpCommunityGroup = snmpCommunityGroup.setStatus('current')
if mibBuilder.loadTexts: snmpCommunityGroup.setDescription('A collection of objects providing basic instrumentation\n            of a SNMP entity which supports community-based\n            authentication.')
snmpSetGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 5)).setObjects(("SNMPv2-MIB", "snmpSetSerialNo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpSetGroup = snmpSetGroup.setStatus('current')
if mibBuilder.loadTexts: snmpSetGroup.setDescription('A collection of objects which allow several cooperating\n            command generator applications to coordinate their\n            use of the set operation.')
systemGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 6)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysObjectID"), ("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysServices"), ("SNMPv2-MIB", "sysORLastChange"), ("SNMPv2-MIB", "sysORID"), ("SNMPv2-MIB", "sysORUpTime"), ("SNMPv2-MIB", "sysORDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systemGroup = systemGroup.setStatus('current')
if mibBuilder.loadTexts: systemGroup.setDescription('The system group defines objects which are common to all\n            managed systems.')
snmpBasicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 7)).setObjects(("SNMPv2-MIB", "coldStart"), ("SNMPv2-MIB", "authenticationFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpBasicNotificationsGroup = snmpBasicNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: snmpBasicNotificationsGroup.setDescription('The basic notifications implemented by an SNMP entity\n        supporting command responder applications.')
snmpWarmStartNotificationGroup = NotificationGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 11)).setObjects(("SNMPv2-MIB", "warmStart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpWarmStartNotificationGroup = snmpWarmStartNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: snmpWarmStartNotificationGroup.setDescription('An additional notification for an SNMP entity supporting\n     command responder applications, if it is able to reinitialize\n     itself such that its configuration is unaltered.')
snmpNotificationGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 12)).setObjects(("SNMPv2-MIB", "snmpTrapOID"), ("SNMPv2-MIB", "snmpTrapEnterprise"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpNotificationGroup = snmpNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: snmpNotificationGroup.setDescription('These objects are required for entities\n            which support notification originator applications.')
snmpOutPkts = MibScalar((1, 3, 6, 1, 2, 1, 11, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutPkts.setStatus('obsolete')
if mibBuilder.loadTexts: snmpOutPkts.setDescription('The total number of SNMP Messages which were\n            passed from the SNMP protocol entity to the\n            transport service.')
snmpInTooBigs = MibScalar((1, 3, 6, 1, 2, 1, 11, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInTooBigs.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInTooBigs.setDescription("The total number of SNMP PDUs which were\n            delivered to the SNMP protocol entity and for\n            which the value of the error-status field was\n            `tooBig'.")
snmpInNoSuchNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInNoSuchNames.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInNoSuchNames.setDescription("The total number of SNMP PDUs which were\n            delivered to the SNMP protocol entity and for\n            which the value of the error-status field was\n            `noSuchName'.")
snmpInBadValues = MibScalar((1, 3, 6, 1, 2, 1, 11, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInBadValues.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInBadValues.setDescription("The total number of SNMP PDUs which were\n            delivered to the SNMP protocol entity and for\n            which the value of the error-status field was\n            `badValue'.")
snmpInReadOnlys = MibScalar((1, 3, 6, 1, 2, 1, 11, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInReadOnlys.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInReadOnlys.setDescription("The total number valid SNMP PDUs which were delivered\n            to the SNMP protocol entity and for which the value\n            of the error-status field was `readOnly'.  It should\n            be noted that it is a protocol error to generate an\n            SNMP PDU which contains the value `readOnly' in the\n            error-status field, as such this object is provided\n            as a means of detecting incorrect implementations of\n            the SNMP.")
snmpInGenErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInGenErrs.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInGenErrs.setDescription("The total number of SNMP PDUs which were delivered\n            to the SNMP protocol entity and for which the value\n            of the error-status field was `genErr'.")
snmpInTotalReqVars = MibScalar((1, 3, 6, 1, 2, 1, 11, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInTotalReqVars.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInTotalReqVars.setDescription('The total number of MIB objects which have been\n            retrieved successfully by the SNMP protocol entity\n            as the result of receiving valid SNMP Get-Request\n            and Get-Next PDUs.')
snmpInTotalSetVars = MibScalar((1, 3, 6, 1, 2, 1, 11, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInTotalSetVars.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInTotalSetVars.setDescription('The total number of MIB objects which have been\n            altered successfully by the SNMP protocol entity as\n            the result of receiving valid SNMP Set-Request PDUs.')
snmpInGetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInGetRequests.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInGetRequests.setDescription('The total number of SNMP Get-Request PDUs which\n            have been accepted and processed by the SNMP\n            protocol entity.')
snmpInGetNexts = MibScalar((1, 3, 6, 1, 2, 1, 11, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInGetNexts.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInGetNexts.setDescription('The total number of SNMP Get-Next PDUs which have been\n            accepted and processed by the SNMP protocol entity.')
snmpInSetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInSetRequests.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInSetRequests.setDescription('The total number of SNMP Set-Request PDUs which\n            have been accepted and processed by the SNMP protocol\n            entity.')
snmpInGetResponses = MibScalar((1, 3, 6, 1, 2, 1, 11, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInGetResponses.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInGetResponses.setDescription('The total number of SNMP Get-Response PDUs which\n            have been accepted and processed by the SNMP protocol\n            entity.')
snmpInTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInTraps.setStatus('obsolete')
if mibBuilder.loadTexts: snmpInTraps.setDescription('The total number of SNMP Trap PDUs which have been\n            accepted and processed by the SNMP protocol entity.')
snmpOutTooBigs = MibScalar((1, 3, 6, 1, 2, 1, 11, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutTooBigs.setStatus('obsolete')
if mibBuilder.loadTexts: snmpOutTooBigs.setDescription("The total number of SNMP PDUs which were generated\n            by the SNMP protocol entity and for which the value\n            of the error-status field was `tooBig.'")
snmpOutNoSuchNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutNoSuchNames.setStatus('obsolete')
if mibBuilder.loadTexts: snmpOutNoSuchNames.setDescription("The total number of SNMP PDUs which were generated\n            by the SNMP protocol entity and for which the value\n            of the error-status was `noSuchName'.")
snmpOutBadValues = MibScalar((1, 3, 6, 1, 2, 1, 11, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutBadValues.setStatus('obsolete')
if mibBuilder.loadTexts: snmpOutBadValues.setDescription("The total number of SNMP PDUs which were generated\n            by the SNMP protocol entity and for which the value\n            of the error-status field was `badValue'.")
snmpOutGenErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutGenErrs.setStatus('obsolete')
if mibBuilder.loadTexts: snmpOutGenErrs.setDescription("The total number of SNMP PDUs which were generated\n            by the SNMP protocol entity and for which the value\n            of the error-status field was `genErr'.")
snmpOutGetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutGetRequests.setStatus('obsolete')
if mibBuilder.loadTexts: snmpOutGetRequests.setDescription('The total number of SNMP Get-Request PDUs which\n            have been generated by the SNMP protocol entity.')
snmpOutGetNexts = MibScalar((1, 3, 6, 1, 2, 1, 11, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutGetNexts.setStatus('obsolete')
if mibBuilder.loadTexts: snmpOutGetNexts.setDescription('The total number of SNMP Get-Next PDUs which have\n            been generated by the SNMP protocol entity.')
snmpOutSetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutSetRequests.setStatus('obsolete')
if mibBuilder.loadTexts: snmpOutSetRequests.setDescription('The total number of SNMP Set-Request PDUs which\n            have been generated by the SNMP protocol entity.')
snmpOutGetResponses = MibScalar((1, 3, 6, 1, 2, 1, 11, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutGetResponses.setStatus('obsolete')
if mibBuilder.loadTexts: snmpOutGetResponses.setDescription('The total number of SNMP Get-Response PDUs which\n            have been generated by the SNMP protocol entity.')
snmpOutTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutTraps.setStatus('obsolete')
if mibBuilder.loadTexts: snmpOutTraps.setDescription('The total number of SNMP Trap PDUs which have\n            been generated by the SNMP protocol entity.')
snmpObsoleteGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 10)).setObjects(("SNMPv2-MIB", "snmpOutPkts"), ("SNMPv2-MIB", "snmpInTooBigs"), ("SNMPv2-MIB", "snmpInNoSuchNames"), ("SNMPv2-MIB", "snmpInBadValues"), ("SNMPv2-MIB", "snmpInReadOnlys"), ("SNMPv2-MIB", "snmpInGenErrs"), ("SNMPv2-MIB", "snmpInTotalReqVars"), ("SNMPv2-MIB", "snmpInTotalSetVars"), ("SNMPv2-MIB", "snmpInGetRequests"), ("SNMPv2-MIB", "snmpInGetNexts"), ("SNMPv2-MIB", "snmpInSetRequests"), ("SNMPv2-MIB", "snmpInGetResponses"), ("SNMPv2-MIB", "snmpInTraps"), ("SNMPv2-MIB", "snmpOutTooBigs"), ("SNMPv2-MIB", "snmpOutNoSuchNames"), ("SNMPv2-MIB", "snmpOutBadValues"), ("SNMPv2-MIB", "snmpOutGenErrs"), ("SNMPv2-MIB", "snmpOutGetRequests"), ("SNMPv2-MIB", "snmpOutGetNexts"), ("SNMPv2-MIB", "snmpOutSetRequests"), ("SNMPv2-MIB", "snmpOutGetResponses"), ("SNMPv2-MIB", "snmpOutTraps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpObsoleteGroup = snmpObsoleteGroup.setStatus('obsolete')
if mibBuilder.loadTexts: snmpObsoleteGroup.setDescription('A collection of objects from RFC 1213 made obsolete\n            by this MIB module.')
mibBuilder.exportSymbols("SNMPv2-MIB", sysUpTime=sysUpTime, snmpInBadVersions=snmpInBadVersions, sysORDescr=sysORDescr, systemGroup=systemGroup, snmpMIBConformance=snmpMIBConformance, snmpNotificationGroup=snmpNotificationGroup, system=system, snmpInBadCommunityNames=snmpInBadCommunityNames, sysORIndex=sysORIndex, snmpInPkts=snmpInPkts, sysORID=sysORID, sysOREntry=sysOREntry, snmpInSetRequests=snmpInSetRequests, snmpInGetResponses=snmpInGetResponses, snmpInASNParseErrs=snmpInASNParseErrs, snmpSilentDrops=snmpSilentDrops, snmpTraps=snmpTraps, snmpOutPkts=snmpOutPkts, snmpBasicComplianceRev2=snmpBasicComplianceRev2, snmpTrapOID=snmpTrapOID, sysLocation=sysLocation, sysObjectID=sysObjectID, snmpSetSerialNo=snmpSetSerialNo, snmpInNoSuchNames=snmpInNoSuchNames, snmpInReadOnlys=snmpInReadOnlys, snmpEnableAuthenTraps=snmpEnableAuthenTraps, snmpOutTooBigs=snmpOutTooBigs, snmpOutGenErrs=snmpOutGenErrs, snmpInGenErrs=snmpInGenErrs, snmp=snmp, snmpInBadValues=snmpInBadValues, snmpTrap=snmpTrap, PYSNMP_MODULE_ID=snmpMIB, snmpOutNoSuchNames=snmpOutNoSuchNames, snmpCommunityGroup=snmpCommunityGroup, snmpMIBCompliances=snmpMIBCompliances, warmStart=warmStart, snmpInTotalSetVars=snmpInTotalSetVars, snmpInGetRequests=snmpInGetRequests, snmpObsoleteGroup=snmpObsoleteGroup, sysDescr=sysDescr, coldStart=coldStart, snmpMIB=snmpMIB, sysORUpTime=sysORUpTime, snmpMIBGroups=snmpMIBGroups, snmpInTooBigs=snmpInTooBigs, snmpMIBObjects=snmpMIBObjects, snmpTrapEnterprise=snmpTrapEnterprise, snmpInTraps=snmpInTraps, snmpInBadCommunityUses=snmpInBadCommunityUses, sysORLastChange=sysORLastChange, sysContact=sysContact, sysORTable=sysORTable, snmpSet=snmpSet, snmpOutTraps=snmpOutTraps, snmpOutBadValues=snmpOutBadValues, snmpSetGroup=snmpSetGroup, snmpWarmStartNotificationGroup=snmpWarmStartNotificationGroup, snmpGroup=snmpGroup, snmpInTotalReqVars=snmpInTotalReqVars, snmpOutGetRequests=snmpOutGetRequests, snmpOutGetNexts=snmpOutGetNexts, authenticationFailure=authenticationFailure, snmpBasicCompliance=snmpBasicCompliance, snmpBasicNotificationsGroup=snmpBasicNotificationsGroup, sysName=sysName, snmpProxyDrops=snmpProxyDrops, sysServices=sysServices, snmpInGetNexts=snmpInGetNexts, snmpOutGetResponses=snmpOutGetResponses, snmpOutSetRequests=snmpOutSetRequests)
