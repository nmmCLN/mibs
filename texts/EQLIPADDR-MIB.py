#
# PySNMP MIB module EQLIPADDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLIPADDR-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:33 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
UTFString, eqlGroupId = mibBuilder.importSymbols("EQLGROUP-MIB", "UTFString", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, IpAddress, MibIdentifier, ModuleIdentity, iso, Gauge32, enterprises, TimeTicks, Unsigned32, Counter64, NotificationType, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "IpAddress", "MibIdentifier", "ModuleIdentity", "iso", "Gauge32", "enterprises", "TimeTicks", "Unsigned32", "Counter64", "NotificationType", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
eqlipaddrModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 9))
eqlipaddrModule.setRevisions(('2002-09-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eqlipaddrModule.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: eqlipaddrModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlipaddrModule.setOrganization('EqualLogic Inc.')
if mibBuilder.loadTexts: eqlipaddrModule.setContactInfo('Contact: Customer Support\n         Postal:  Dell Inc\n                  300 Innovative Way, Suite 301, Nashua, NH 03062\n         Tel:     +1 603-579-9762\n         E-mail:  US-NH-CS-TechnicalSupport@dell.com\n         WEB:     www.equallogic.com')
if mibBuilder.loadTexts: eqlipaddrModule.setDescription('Equallogic Inc. Storage Array IP address table mib\n\n         Copyright (c) 2002-2010 by Dell, Inc.\n\n         All rights reserved.  This software may not be copied, disclosed,\n         transferred, or used except in accordance with a license granted\n         by Dell, Inc.  This software embodies proprietary information\n         and trade secrets of Dell, Inc.\n        ')
eqlipAddrTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 9, 1), )
if mibBuilder.loadTexts: eqlipAddrTable.setStatus('deprecated')
if mibBuilder.loadTexts: eqlipAddrTable.setDescription("EqualLogic-Dynamic Storage Volume Table. \n                             The table of addressing information relevant to\n                             this entity's IP addresses.")
eqlipAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 9, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLIPADDR-MIB", "eqlIpAdEntAddr"))
if mibBuilder.loadTexts: eqlipAddrEntry.setStatus('current')
if mibBuilder.loadTexts: eqlipAddrEntry.setDescription("The addressing information for one of this\n                            entity's IP addresses.")
eqlIpAdEntAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: eqlIpAdEntAddr.setStatus('current')
if mibBuilder.loadTexts: eqlIpAdEntAddr.setDescription("The IP address to which this entry's addressing\n                            information pertains.")
eqlIpAdEntIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpAdEntIfName.setStatus('current')
if mibBuilder.loadTexts: eqlIpAdEntIfName.setDescription("The interface name for which this entry's addressing\n                            information pertains.")
eqlIpAdEntNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpAdEntNetMask.setStatus('current')
if mibBuilder.loadTexts: eqlIpAdEntNetMask.setDescription('The subnet mask associated with the IP address of\n                             this entry.  The value of the mask is an IP\n                             address with all the network bits set to 1 and all\n                             the hosts bits set to 0.')
eqlIpAdEntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpAdEntIfIndex.setStatus('current')
if mibBuilder.loadTexts: eqlIpAdEntIfIndex.setDescription("The interface index for which this entry's addressing\n                            information pertains.")
eqlIpAdEntRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpAdEntRowStatus.setStatus('current')
if mibBuilder.loadTexts: eqlIpAdEntRowStatus.setDescription("The status of this conceptual row.\n\n                 Until instances of all read-create columns are\n                 appropriately configured, the value of the\n                 corresponding instance of the eqlIpRowStatus column\n                 is 'notReady'.\n\n                 The  RowStatus TC [RFC1903] requires that this\n                 DESCRIPTION clause states under which circumstances\n                 other objects in this row can be modified:\n\n                 The value of this object has no effect on whether\n                 other objects in this conceptual row can be modified.\n                ")
eqlifTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 9, 2), )
if mibBuilder.loadTexts: eqlifTable.setStatus('current')
if mibBuilder.loadTexts: eqlifTable.setDescription("EqualLogic-Persistent Interfaces Table. \n                             The table of information relevant to\n                             this entity's physical interfaces.")
eqlifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 9, 2, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eqlifEntry.setStatus('current')
if mibBuilder.loadTexts: eqlifEntry.setDescription(' ')
eqlifDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlifDescr.setStatus('current')
if mibBuilder.loadTexts: eqlifDescr.setDescription('This field provides a writable area for a manager to \n                                enter user specific data pertaining to the interface \n                                referred by this instance of ifIndex ')
eqlifPortAttr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("attr-pss-only", 1), ("attr-initiator-only", 2), ("attr-any", 3))).clone('attr-any')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlifPortAttr.setStatus('current')
if mibBuilder.loadTexts: eqlifPortAttr.setDescription('This field specifies the mode of the specified port as follows:')
eqlifAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlifAdminStatus.setStatus('current')
if mibBuilder.loadTexts: eqlifAdminStatus.setDescription('\n                      The desired state of the interface.  The\n                      testing(3) state indicates that no operational\n                      packets can be passed. \n                      This column is used to maintain the desired state of the \n                      interface accross reboots. The value of this object MUST \n                      always be equal to ifAdminStatus defined in rfc1213 mib.')
eqlifRole = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("iscsi-only", 0), ("mgmt-only", 1))).clone('iscsi-only')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlifRole.setStatus('current')
if mibBuilder.loadTexts: eqlifRole.setDescription('\n                      The desired role of the interface. By default the interface will allow\n                      iscsi only traffic. when set to mgmt-only, only management traffic\n                      will be allowed. (There is not a both at this time)')
eqlWKATable = MibTable((1, 3, 6, 1, 4, 1, 12740, 9, 3), )
if mibBuilder.loadTexts: eqlWKATable.setStatus('current')
if mibBuilder.loadTexts: eqlWKATable.setDescription('EqualLogic-Persistent WKA Table. This table maintains the list of\n                     well known ipaddresses (WKA) in the group.')
eqlWKAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 9, 3, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLIPADDR-MIB", "eqlInetAddrEntAddrType"), (0, "EQLIPADDR-MIB", "eqlInetAddrEntAddr"))
if mibBuilder.loadTexts: eqlWKAEntry.setStatus('current')
if mibBuilder.loadTexts: eqlWKAEntry.setDescription('An entry (row) containing storage group WKA information.')
eqlWKARowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlWKARowStatus.setStatus('current')
if mibBuilder.loadTexts: eqlWKARowStatus.setDescription('The status of this conceptual row.')
eqlWKARole = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("management", 1), ("secondary", 2))).clone('secondary')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlWKARole.setStatus('current')
if mibBuilder.loadTexts: eqlWKARole.setDescription(" The role of this WKA. Management WKA is used for only management traffic. secondary WKA can be used incase the \n                    of failover to secondary site and secondary site wants to use primary site's WKA. Secondary WKAs can exist\n                    independent of partner records and their ipaddresses.")
eqlifStatusTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 9, 4), )
if mibBuilder.loadTexts: eqlifStatusTable.setStatus('current')
if mibBuilder.loadTexts: eqlifStatusTable.setDescription('EqualLogic-Dynamic Interface Table.\n                     This table contains WKA information about the interfaces.')
eqlifStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 9, 4, 1), )
eqlifEntry.registerAugmentions(("EQLIPADDR-MIB", "eqlifStatusEntry"))
eqlifStatusEntry.setIndexNames(*eqlifEntry.getIndexNames())
if mibBuilder.loadTexts: eqlifStatusEntry.setStatus('current')
if mibBuilder.loadTexts: eqlifStatusEntry.setDescription('An entry (row) containing Interface WKA information.')
eqlifStatusMgmtRolePolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("non-configurable", 0), ("configurable", 1), ("fixed", 2))).clone('non-configurable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlifStatusMgmtRolePolicy.setStatus('current')
if mibBuilder.loadTexts: eqlifStatusMgmtRolePolicy.setDescription('\n                     This field is for specifying the policy of this interface, i.e whether this interface can be used for mgmt-only role.')
eqlifStatusConfigurationFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 4, 1, 2), Bits().clone(namedValues=NamedValues(("isDcbCapable", 0), ("flag1", 1), ("flag2", 2), ("flag3", 3), ("flag4", 4), ("flag5", 5), ("flag6", 6), ("flag7", 7), ("flag8", 8), ("flag9", 9), ("flag10", 10), ("flag11", 11), ("flag12", 12), ("flag13", 13), ("flag14", 14), ("flag15", 15), ("flag16", 16), ("flag17", 17), ("flag18", 18), ("flag19", 19), ("flag20", 20), ("flag21", 21), ("flag22", 22), ("flag23", 23), ("flag24", 24), ("flag25", 25), ("flag26", 26), ("flag27", 27), ("flag28", 28), ("flag29", 29), ("flag30", 30), ("flag31", 31)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlifStatusConfigurationFlags.setStatus('current')
if mibBuilder.loadTexts: eqlifStatusConfigurationFlags.setDescription('This fields defines the common place holder for ethernet interface\n                     configuration flags.  The flags must be of type\n                     enable(1) or disable(0), and the default will always be disable(0).')
eqlifOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlifOperStatus.setStatus('current')
if mibBuilder.loadTexts: eqlifOperStatus.setDescription('The current operational state of the interface.  The\n               testing(3) state indicates that no operational packets\n               can be passed.  If eqlifAdminStatus is down(2) then\n               eqlifOperStatus should be down(2).  If eqlifAdminStatus is\n               changed to up(1) then eqlifOperStatus should change to\n               up(1) if the interface is ready to transmit and\n               receive network traffic; it should change to\n               dormant(5) if the interface is waiting for external\n               actions (such as a serial line waiting for an\n               incomming connection); it should remain in the down(2)\n               state if and only if there is a fault that prevents if\n               from going to the up(1) state.')
eqlinetAddrTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 9, 5), )
if mibBuilder.loadTexts: eqlinetAddrTable.setStatus('current')
if mibBuilder.loadTexts: eqlinetAddrTable.setDescription("EqualLogic-Persistent Storage Volume Table. \n                             The table of addressing information relevant to\n                             this entity's IP addresses.")
eqlinetAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 9, 5, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLIPADDR-MIB", "eqlInetAddrEntAddrType"), (0, "EQLIPADDR-MIB", "eqlInetAddrEntAddr"))
if mibBuilder.loadTexts: eqlinetAddrEntry.setStatus('current')
if mibBuilder.loadTexts: eqlinetAddrEntry.setDescription("The addressing information for one of this\n                            entity's IP addresses.")
eqlInetAddrEntAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 1), InetAddressType())
if mibBuilder.loadTexts: eqlInetAddrEntAddrType.setStatus('current')
if mibBuilder.loadTexts: eqlInetAddrEntAddrType.setDescription("The IP address to which this entry's addressing\n                            information pertains.")
eqlInetAddrEntAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 2), InetAddress())
if mibBuilder.loadTexts: eqlInetAddrEntAddr.setStatus('current')
if mibBuilder.loadTexts: eqlInetAddrEntAddr.setDescription("The IP address to which this entry's addressing\n                            information pertains.")
eqlInetAddrEntIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlInetAddrEntIfName.setStatus('current')
if mibBuilder.loadTexts: eqlInetAddrEntIfName.setDescription("The interface name for which this entry's addressing\n                            information pertains.")
eqlInetAddrEntNetMaskType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 4), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlInetAddrEntNetMaskType.setStatus('current')
if mibBuilder.loadTexts: eqlInetAddrEntNetMaskType.setDescription('The subnet mask associated with the IP address of\n                             this entry.  The value of the mask is an IP\n                             address with all the network bits set to 1 and all\n                             the hosts bits set to 0.')
eqlInetAddrEntNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlInetAddrEntNetMask.setStatus('current')
if mibBuilder.loadTexts: eqlInetAddrEntNetMask.setDescription('The subnet mask associated with the IP address of\n                             this entry.  The value of the mask is an IP\n                             address with all the network bits set to 1 and all\n                             the hosts bits set to 0.')
eqlInetAddrEntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlInetAddrEntIfIndex.setStatus('current')
if mibBuilder.loadTexts: eqlInetAddrEntIfIndex.setDescription("The interface index for which this entry's addressing\n                            information pertains.")
eqlInetAddrEntFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no-options", 0), ("static", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlInetAddrEntFlags.setStatus('current')
if mibBuilder.loadTexts: eqlInetAddrEntFlags.setDescription('This specifies specific flags for the address.  \n                            Currently the only flag that can be set is static (1),\n                            which means the address has been statically\n                            configured by the administrator')
eqlInetAddrEntRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlInetAddrEntRowStatus.setStatus('current')
if mibBuilder.loadTexts: eqlInetAddrEntRowStatus.setDescription("The status of this conceptual row.\n\n                 Until instances of all read-create columns are\n                 appropriately configured, the value of the\n                 corresponding instance of the eqlIpRowStatus column\n                 is 'notReady'.\n\n                 The  RowStatus TC [RFC1903] requires that this\n                 DESCRIPTION clause states under which circumstances\n                 other objects in this row can be modified:\n\n                 The value of this object has no effect on whether\n                 other objects in this conceptual row can be modified.\n                ")
mibBuilder.exportSymbols("EQLIPADDR-MIB", eqlInetAddrEntAddrType=eqlInetAddrEntAddrType, eqlInetAddrEntFlags=eqlInetAddrEntFlags, eqlifTable=eqlifTable, eqlInetAddrEntNetMaskType=eqlInetAddrEntNetMaskType, eqlifStatusTable=eqlifStatusTable, eqlIpAdEntIfName=eqlIpAdEntIfName, eqlInetAddrEntIfName=eqlInetAddrEntIfName, eqlInetAddrEntIfIndex=eqlInetAddrEntIfIndex, eqlifAdminStatus=eqlifAdminStatus, eqlifPortAttr=eqlifPortAttr, eqlIpAdEntAddr=eqlIpAdEntAddr, eqlWKATable=eqlWKATable, eqlifRole=eqlifRole, eqlipaddrModule=eqlipaddrModule, eqlinetAddrTable=eqlinetAddrTable, eqlinetAddrEntry=eqlinetAddrEntry, eqlifEntry=eqlifEntry, eqlWKAEntry=eqlWKAEntry, eqlifStatusConfigurationFlags=eqlifStatusConfigurationFlags, eqlIpAdEntIfIndex=eqlIpAdEntIfIndex, eqlifStatusMgmtRolePolicy=eqlifStatusMgmtRolePolicy, eqlipAddrEntry=eqlipAddrEntry, eqlIpAdEntNetMask=eqlIpAdEntNetMask, eqlifStatusEntry=eqlifStatusEntry, eqlipAddrTable=eqlipAddrTable, eqlifOperStatus=eqlifOperStatus, eqlInetAddrEntNetMask=eqlInetAddrEntNetMask, eqlInetAddrEntRowStatus=eqlInetAddrEntRowStatus, eqlWKARole=eqlWKARole, PYSNMP_MODULE_ID=eqlipaddrModule, eqlIpAdEntRowStatus=eqlIpAdEntRowStatus, eqlifDescr=eqlifDescr, eqlInetAddrEntAddr=eqlInetAddrEntAddr, eqlWKARowStatus=eqlWKARowStatus)
