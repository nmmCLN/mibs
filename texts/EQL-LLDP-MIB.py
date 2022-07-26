#
# PySNMP MIB module EQL-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQL-LLDP-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:44 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, MibIdentifier, TimeTicks, ObjectIdentity, Unsigned32, IpAddress, NotificationType, enterprises, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "enterprises", "Counter32")
MacAddress, TimeInterval, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TimeInterval", "DisplayString", "TextualConvention", "TruthValue")
eqlLldpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 21))
eqlLldpMib.setRevisions(('2010-07-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eqlLldpMib.setRevisionsDescriptions(('Initial revision - based on IEEE 802.1AB-2009 Copyright (C) IEEE.',))
if mibBuilder.loadTexts: eqlLldpMib.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlLldpMib.setOrganization('EqualLogic Inc.')
if mibBuilder.loadTexts: eqlLldpMib.setContactInfo('Contact: Customer Support\n         Postal:  Dell Inc\n                  300 Innovative Way, Suite 301, Nashua, NH 03062\n         Tel:     +1 603-579-9762\n         E-mail:  US-NH-CS-TechnicalSupport@dell.com\n         WEB:     www.equallogic.com')
if mibBuilder.loadTexts: eqlLldpMib.setDescription('Link Layer Discovery Protocol MIB module.\n        Copyright (c) 2010-2012 by Dell Inc.\n\n        All rights reserved.  This software may not be copied, disclosed,\n        transferred, or used except in accordance with a license granted\n        by Dell Inc.  This software embodies proprietary information\n        and trade secrets of Dell Inc.\n\n        Copyright (C) IEEE (2009). This version of this MIB module\n        is published as subclause 11.5.1 of IEEE Std 802.1AB-2009;\n        see the standard itself for full legal notices.')
eqlLldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 21, 1))
class EqlLldpV2ChassisIdSubtype(TextualConvention, Integer32):
    description = 'This describes the source of a chassis identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7))

class EqlLldpV2ChassisId(TextualConvention, OctetString):
    description = 'This describes the format of a chassis identifier string.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(255, 255)
    fixedLength = 255

class EqlLldpV2PortIdSubtype(TextualConvention, Integer32):
    description = 'This describes the source of a particular type of port\n        identifier used in the LLDP MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7))

class EqlLldpV2PortId(TextualConvention, OctetString):
    description = 'This describes the format of a port identifier string.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class EqlLldpV2State(TextualConvention, Integer32):
    description = 'This describes the state of LLDP for the port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("off", 0), ("noPeer", 1), ("active", 2), ("multiplePeers", 3))

eqlLldpDynamicIfTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1), )
if mibBuilder.loadTexts: eqlLldpDynamicIfTable.setStatus('current')
if mibBuilder.loadTexts: eqlLldpDynamicIfTable.setDescription("EqualLogic-Dynamic\n        A table of LLDP information per each interface of a system.\n        Each row in this table supplies values for one port's\n        LLDP parameters.")
eqlLldpDynamicIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eqlLldpDynamicIfEntry.setStatus('current')
if mibBuilder.loadTexts: eqlLldpDynamicIfEntry.setDescription('An entry in the LLDP table, containing information\n        about LLDP on a single interface.')
eqlLldpRemMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpRemMacAddress.setStatus('current')
if mibBuilder.loadTexts: eqlLldpRemMacAddress.setDescription('The MAC address associated with the LLDP peer.')
eqlLldpV2RemChassisIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 2), EqlLldpV2ChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemChassisIdSubtype.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemChassisIdSubtype.setDescription('The type of encoding used to identify the chassis\n        associated with the remote system.')
eqlLldpV2RemChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 3), EqlLldpV2ChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemChassisId.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemChassisId.setDescription('The string value used to identify the chassis component\n        associated with the remote system.')
eqlLldpV2RemPortIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 4), EqlLldpV2PortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortIdSubtype.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemPortIdSubtype.setDescription('The type of encoding used to identify the port\n        associated with the remote system.')
eqlLldpV2RemPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 5), EqlLldpV2PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortId.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemPortId.setDescription('The string value used to identify the port component\n        associated with the remote system.')
eqlLldpV2RemPortDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemPortDesc.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemPortDesc.setDescription('The string value used to identify the description of\n        the given port associated with the remote system.')
eqlLldpV2RemSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemSysName.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemSysName.setDescription('The string value used to identify the system name of the\n        remote system.')
eqlLldpV2RemSysDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemSysDesc.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemSysDesc.setDescription('The string value used to identify the system description\n        of the remote system.')
eqlLldpV2State = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 9), EqlLldpV2State()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2State.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2State.setDescription('The current LLDP state for the port.')
eqlLldpV2RemMgmtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlLldpV2RemMgmtAddr.setStatus('current')
if mibBuilder.loadTexts: eqlLldpV2RemMgmtAddr.setDescription('The management address reported by the remote system.\n\n        If multiple addresses were reported, they are delimited by\n        commas.')
mibBuilder.exportSymbols("EQL-LLDP-MIB", eqlLldpV2RemPortIdSubtype=eqlLldpV2RemPortIdSubtype, EqlLldpV2PortId=EqlLldpV2PortId, eqlLldpV2RemSysName=eqlLldpV2RemSysName, eqlLldpV2State=eqlLldpV2State, PYSNMP_MODULE_ID=eqlLldpMib, eqlLldpDynamicIfTable=eqlLldpDynamicIfTable, eqlLldpV2RemMgmtAddr=eqlLldpV2RemMgmtAddr, eqlLldpDynamicIfEntry=eqlLldpDynamicIfEntry, eqlLldpV2RemPortId=eqlLldpV2RemPortId, EqlLldpV2ChassisIdSubtype=EqlLldpV2ChassisIdSubtype, eqlLldpMIBObjects=eqlLldpMIBObjects, eqlLldpRemMacAddress=eqlLldpRemMacAddress, EqlLldpV2ChassisId=EqlLldpV2ChassisId, eqlLldpV2RemChassisId=eqlLldpV2RemChassisId, eqlLldpV2RemPortDesc=eqlLldpV2RemPortDesc, eqlLldpV2RemSysDesc=eqlLldpV2RemSysDesc, eqlLldpV2RemChassisIdSubtype=eqlLldpV2RemChassisIdSubtype, EqlLldpV2PortIdSubtype=EqlLldpV2PortIdSubtype, eqlLldpMib=eqlLldpMib, EqlLldpV2State=EqlLldpV2State)
