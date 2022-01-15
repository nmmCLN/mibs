#
# PySNMP MIB module DOCS-SEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DOCS-SEC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
clabProjDocsis, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjDocsis")
docsIf3CmtsCmRegStatusId, docsIf3CmtsCmRegStatusEntry = mibBuilder.importSymbols("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId", "docsIf3CmtsCmRegStatusEntry")
InetAddress, InetAddressType, InetAddressPrefixLength, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetAddressPrefixLength", "InetPortNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
SnmpTagList, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "SnmpTagList")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, iso, Integer32, Counter32, Bits, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "iso", "Integer32", "Counter32", "Bits", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, DateAndTime, MacAddress, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "MacAddress", "TruthValue", "TextualConvention", "RowStatus")
docsSecMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11))
docsSecMib.setRevisions(('2007-02-23 00:00', '2006-12-07 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: docsSecMib.setRevisionsDescriptions(('Revised Version includes ECN OSSIv3.0-N-06.0357-1\n        and published as IO2', 'Initial version, published as part of the CableLabs\n        OSSIv3.0 specification CM-SP-OSSIv3.0-I01-061207\n        Copyright 1999-2006 Cable Television Laboratories, Inc.\n        All rights reserved.',))
if mibBuilder.loadTexts: docsSecMib.setLastUpdated('200702230000Z')
if mibBuilder.loadTexts: docsSecMib.setOrganization('Cable Television Laboratories, Inc.')
if mibBuilder.loadTexts: docsSecMib.setContactInfo('Postal: Cable Television Laboratories, Inc.\n            858 Coal Creek Circle\n            Louisville, Colorado 80027-9750\n            U.S.A.\n            Phone: +1 303-661-9100\n            Fax:   +1 303-661-9199\n            E-mail: mibs@cablelabs.com')
if mibBuilder.loadTexts: docsSecMib.setDescription('This MIB module contains the management objects for \n        the management of the security requirements in the DOCSIS\n        Security Specification.')
docsSecMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1))
docsSecCmtsServerCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 1))
docsSecCmtsServerCfgTftpOptions = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 1, 1), Bits().clone(namedValues=NamedValues(("hwAddr", 0), ("netAddr", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSecCmtsServerCfgTftpOptions.setReference('DOCSIS 3.0 Operations Support System Interface\n         Specification CM-SP-OSSIv3.0-I01-061207,\n         MdCfg Object Section in the Media Access Control (MAC)\n         Requirements Annex.')
if mibBuilder.loadTexts: docsSecCmtsServerCfgTftpOptions.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsServerCfgTftpOptions.setDescription("This attribute instructs the CMTS to insert the source\n        IP address and/or MAC address of received TFTP packets\n        into the TFTP option fields before forwarding\n        the packets to the Config File server.\n        This attribute is only applicable when the TftpProxyEnabled\n        attribute of the MdCfg object is 'true'.")
docsSecCmtsServerCfgConfigFileLearningEnable = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSecCmtsServerCfgConfigFileLearningEnable.setReference('DOCSIS 3.0 Operations Support System Interface\n         Specification CM-SP-OSSIv3.0-I01-061207,\n         MdCfg Object Section in the Media Access Control (MAC)\n         Requirements Annex.\n         DOCSIS 3.0 Security Specification\n         CM-SP-SECv3.0-I01-060804, Secure Provisioning Section.\n         DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804.')
if mibBuilder.loadTexts: docsSecCmtsServerCfgConfigFileLearningEnable.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsServerCfgConfigFileLearningEnable.setDescription("This attribute enables and disables Configuration\n        File Learning functionality.\n        If this attribute is set to 'true' the CMTS will respond\n        with Authentication Failure in the REG-RSP message\n        when there is a mismatch between learned config file\n        parameters and REG-REQ parameters. If this attribute\n        is set to 'false', the CMTS will not execute config\n        file learning and mismatch check.\n        This attribute is only applicable when the TftpProxyEnabled\n        attribute of the MdCfg object is 'true'.")
docsSecCmtsEncrypt = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 2))
docsSecCmtsEncryptEncryptAlgPriority = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 2, 1), SnmpTagList().clone('aes128CbcMode des56CbcMode des40CbcMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSecCmtsEncryptEncryptAlgPriority.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsEncryptEncryptAlgPriority.setDescription('This attribute allows for configuration of a prioritized\n        list of encryption algorithms the CMTS will\n        use when selecting the primary SAID encryption algorithm\n        for a given CM. The CMTS selects the highest priority\n        encryption algorithm from this list that the CM\n        supports. By default the following encryption algorithms\n        are listed from highest to lowest priority (left\n        being the highest): 128 bit AES, 56 bit DES, 40 bit\n        DES.\n        An empty list indicates that the CMTS attempts to use\n        the latest and robust encryption algorithm supported\n        by the CM. The CMTS will ignore unknown values or unsupported\n        algorithms.')
docsSecCmtsCmEaeExclusionTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3), )
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionTable.setReference('DOCSIS 3.0 Operations Support System Interface\n         Specification CM-SP-OSSIv3.0-I01-061207,\n         MdCfg Object Section in the Media Access Control (MAC)\n         Requirements Annex.\n         DOCSIS 3.0 Security Specification\n         CM-SP-SECv3.0-I01-060804, Early Authentication And\n         Encryption (EAE) Section.')
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionTable.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionTable.setDescription('This object defines a list of CMs or CM groups to exclude\n        from Early Authentication and Encryption (EAE).\n        This object allows overrides to the value of EAE Control\n        for individual CMs or group of CMs for purposes\n        such as debugging. The CMTS supports a minimum of\n        30 instances of the CmtsCmEaeExclusion object.\n        This object is only applicable when the EarlyAuthEncryptCtrl\n        attribute of the MdCfg object is enabled.\n\n        This object supports the creation and deletion of multiple\n        instances.')
docsSecCmtsCmEaeExclusionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3, 1), ).setIndexNames((0, "DOCS-SEC-MIB", "docsSecCmtsCmEaeExclusionId"))
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionEntry.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionEntry.setDescription('The conceptual row of docsSecCmtsCmEaeExclusion.\n        The CMTS persists all instances of CmtsCmEaeExclusion\n        across reinitializations.')
docsSecCmtsCmEaeExclusionId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionId.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionId.setDescription('This key uniquely identifies the exclusion MAC address\n        rule.')
docsSecCmtsCmEaeExclusionMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3, 1, 2), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionMacAddr.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionMacAddr.setDescription('This attribute identifies the CM MAC address. A match\n        is made when a CM MAC address bitwise ANDed with the\n        MacAddrMask attribute equals the value of this attribute.')
docsSecCmtsCmEaeExclusionMacAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3, 1, 3), MacAddress().clone(hexValue="FFFFFFFFFFFF")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionMacAddrMask.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionMacAddrMask.setDescription('This attribute identifies the CM MAC address mask\n        and is used with the MacAddr attribute.')
docsSecCmtsCmEaeExclusionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionRowStatus.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCmEaeExclusionRowStatus.setDescription('Controls and reflects the status of rows in this\n        table. There is no restriction on changing values in\n        a row of this table while the row is active.')
docsSecCmtsSavControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 4))
docsSecCmtsSavControlCmAuthEnable = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 4, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSecCmtsSavControlCmAuthEnable.setReference('DOCSIS 3.0 Operations Support System Interface\n         Specification CM-SP-OSSIv3.0-I01-061207,\n         MdCfg Object Section in the Media Access Control (MAC)\n         Requirements Annex.')
if mibBuilder.loadTexts: docsSecCmtsSavControlCmAuthEnable.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsSavControlCmAuthEnable.setDescription("This attribute enables or disables Source Address\n        Verification (SAV) for CM configured policies in the\n        SavCmAuth object. If this attribute is set to 'false',\n        the CM configured policies in the SavCmAuth object\n        are ignored.\n        This attribute is only applicable when the\n        SrcAddrVerificationEnabled attribute of the MdCfg object is\n        'true'.")
docsSecSavCmAuthTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 5), )
if mibBuilder.loadTexts: docsSecSavCmAuthTable.setReference('DOCSIS 3.0 Operations Support System Interface\n         Specification CM-SP-OSSIv3.0-I01-061207,\n         MdCfg Object Section in the Media Access Control (MAC)\n         Requirements Annex.\n         DOCSIS 3.0 Security Specification\n         CM-SP-SECv3.0-I01-060804, Secure Provisioning Section.\n         DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804,\n         Common Radio Frequency Interface Encodings Annex.')
if mibBuilder.loadTexts: docsSecSavCmAuthTable.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCmAuthTable.setDescription("This object defines a read-only set of SAV policies\n        associated with a CM that the CMTS will use in addition\n        to the CMTS verification of an operator assigned IP\n        Address being associated with a CM. When the CMTS has\n        not resolved a source address of a CM CPE, the CMTS verifies\n        if the CM CPE is authorized to pass traffic based\n        on this object. These object policies include a list\n        of subnet prefixes (defined in the SavStaticList\n        object) or a SAV Group Name that could reference a CMTS\n        configured list of subnet prefixes (defined in SavCfgList\n        object) or vendor-specific policies. The CMTS\n        populates the attributes of this object for a CM from\n        that CM's config file.\n        This object is only applicable when the\n        SrcAddrVerificationEnabled attribute of the MdCfg object is\n        'true' and the CmAuthEnable attribute of the CmtsSavCtrl\n        object is 'true'.\n        The CMTS is not required to persist instances of this\n        object across reinitializations.")
docsSecSavCmAuthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 5, 1), ).setIndexNames((0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"))
if mibBuilder.loadTexts: docsSecSavCmAuthEntry.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCmAuthEntry.setDescription('The conceptual row of docsSecSavCmAuth.')
docsSecSavCmAuthGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 5, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSecSavCmAuthGrpName.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804,\n         Common Radio Frequency Interface Encodings Annex.')
if mibBuilder.loadTexts: docsSecSavCmAuthGrpName.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCmAuthGrpName.setDescription('This attribute references the Name attribute of the\n        SavCfgList object of a CM. If the CM signaled group\n        name is not configured in the CMTS, the CMTS ignores this\n        attribute value for the purpose of Source Address\n        Verification. The CMTS must allow the modification\n        of the GrpName object and use the updated SAV rules for\n        newly discovered CPEs from CMs. When a source IP address\n        is claimed by two CMs (e.g., detected as duplicated),\n        the CMTS must use the current SAV rules defined\n        for both CMs in case the SAV GrpName rules may have been\n        updated. In the case of a persisting conflict, it is\n        up to vendor-implementation to decide what CM should\n        hold the SAV authorization.\n        The zero-length string indicates that no SAV Group was\n        signaled by the CM. The zero-length value or a non-existing\n        reference in the SavCfgList object means the\n        SavCfgListName is ignored for the purpose of SAV.')
docsSecSavCmAuthStaticPrefixListId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSecSavCmAuthStaticPrefixListId.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCmAuthStaticPrefixListId.setDescription('This attribute identifies the reference to a CMTS\n        created subnet prefix list based on the CM signaled static\n        prefix list TLV elements. The CMTS may reuse this\n        attribute value to reference more than one CM when\n        those CMs have signaled the same subnet prefix list to\n        the CMTS.\n        The value zero indicates that no SAV static prefix encodings\n        were signaled by the CM.')
docsSecSavCfgListTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6), )
if mibBuilder.loadTexts: docsSecSavCfgListTable.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCfgListTable.setDescription('This object defines the CMTS configured subnet prefix\n        extension to the SavCmAuth object.\n        This object supports the creation and deletion of multiple\n        instances.\n        Creation of a new instance of this object requires the\n        PrefixAddrType and PrefixAddr attributes to be set.')
docsSecSavCfgListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1), ).setIndexNames((0, "DOCS-SEC-MIB", "docsSecSavCfgListName"), (0, "DOCS-SEC-MIB", "docsSecSavCfgListRuleId"))
if mibBuilder.loadTexts: docsSecSavCfgListEntry.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCfgListEntry.setDescription('The conceptual row of docsSecSavCfgList.\n        The CMTS persists all instances of SavCfgList\n        across reinitializations.')
docsSecSavCfgListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: docsSecSavCfgListName.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCfgListName.setDescription('This attribute is the key that identifies the instance\n        of the SavCmAuth object to which this object extension\n        belongs.')
docsSecSavCfgListRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: docsSecSavCfgListRuleId.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCfgListRuleId.setDescription('This attribute is the key that identifies a particular\n        subnet prefix rule of an instance of this object.')
docsSecSavCfgListPrefixAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSecSavCfgListPrefixAddrType.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCfgListPrefixAddrType.setDescription('This attribute identifies the IP address type of this\n        subnet prefix rule.')
docsSecSavCfgListPrefixAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSecSavCfgListPrefixAddr.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCfgListPrefixAddr.setDescription('This attribute corresponds to the IP address of this\n        subnet prefix rule in accordance to the PrefixAddrType\n        attribute.')
docsSecSavCfgListPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 5), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSecSavCfgListPrefixLen.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCfgListPrefixLen.setDescription('This attribute defines the length of the subnet prefix\n        to be matched by this rule.')
docsSecSavCfgListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 6, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsSecSavCfgListRowStatus.setStatus('current')
if mibBuilder.loadTexts: docsSecSavCfgListRowStatus.setDescription('The row creation control of this conceptual row.\n        An entry in this table can be set to active\n        only when the following attributes are correctly\n        assigned:\n           PrefixAddrType\n           PrefixAddress\n        There are no restrictions to modify or delete\n        entries in this table.')
docsSecSavStaticListTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7), )
if mibBuilder.loadTexts: docsSecSavStaticListTable.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n        Specification CM-SP-MULPIv3.0-I01-060804,\n        Common Radio Frequency Interface Encodings Annex.')
if mibBuilder.loadTexts: docsSecSavStaticListTable.setStatus('current')
if mibBuilder.loadTexts: docsSecSavStaticListTable.setDescription('This object defines a subnet prefix extension to the\n        SavCmAuth object based on CM statically signaled\n        subnet prefixes to the CMTS.\n        When a CM signals to the CMTS static subnet prefixes,\n        the CMTS must create a List Id to be referenced by the CM\n        in the SavCmAuth StaticPrefixListId attribute, or\n        the CMTS may reference an existing List Id associated\n        to previously registered CMs in case of those subnet\n        prefixes associated with the List Id match the ones\n        signaled by the CM.')
docsSecSavStaticListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1), ).setIndexNames((0, "DOCS-SEC-MIB", "docsSecSavStaticListId"), (0, "DOCS-SEC-MIB", "docsSecSavStaticListRuleId"))
if mibBuilder.loadTexts: docsSecSavStaticListEntry.setStatus('current')
if mibBuilder.loadTexts: docsSecSavStaticListEntry.setDescription('The conceptual row of docsSecSavStaticList.\n        The CMTS may persist instances of this object\n        across reinitializations.')
docsSecSavStaticListId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: docsSecSavStaticListId.setStatus('current')
if mibBuilder.loadTexts: docsSecSavStaticListId.setDescription('This key uniquely identifies the index that groups\n        multiple subnet prefix rules. The CMTS assigns this\n        value per CM or may reuse it among multiple CMs that share\n        the same list of subnet prefixes.')
docsSecSavStaticListRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: docsSecSavStaticListRuleId.setStatus('current')
if mibBuilder.loadTexts: docsSecSavStaticListRuleId.setDescription('This key identifies a particular static subnet prefix\n        rule of an instance of this object.')
docsSecSavStaticListPrefixAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSecSavStaticListPrefixAddrType.setStatus('current')
if mibBuilder.loadTexts: docsSecSavStaticListPrefixAddrType.setDescription('This attribute identifies the IP address type of this\n        subnet prefix rule.')
docsSecSavStaticListPrefixAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSecSavStaticListPrefixAddr.setStatus('current')
if mibBuilder.loadTexts: docsSecSavStaticListPrefixAddr.setDescription('This attribute corresponds to the IP address of this\n        subnet prefix rule in accordance to the PrefixAddrType\n        attribute.')
docsSecSavStaticListPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 7, 1, 5), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSecSavStaticListPrefixLen.setStatus('current')
if mibBuilder.loadTexts: docsSecSavStaticListPrefixLen.setDescription('This attribute defines the length of the subnet prefix\n        to be matched by this rule.')
docsSecCmtsCmSavStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 8), )
if mibBuilder.loadTexts: docsSecCmtsCmSavStatsTable.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCmSavStatsTable.setDescription('This object provides a read-only list of SAV counters\n        for different service theft indications.')
docsSecCmtsCmSavStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 8, 1), )
docsIf3CmtsCmRegStatusEntry.registerAugmentions(("DOCS-SEC-MIB", "docsSecCmtsCmSavStatsEntry"))
docsSecCmtsCmSavStatsEntry.setIndexNames(*docsIf3CmtsCmRegStatusEntry.getIndexNames())
if mibBuilder.loadTexts: docsSecCmtsCmSavStatsEntry.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCmSavStatsEntry.setDescription('The conceptual row of docsSecCmtsCmSavStats.')
docsSecCmtsCmSavStatsSavDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 8, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSecCmtsCmSavStatsSavDiscards.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCmSavStatsSavDiscards.setDescription('This attribute provides the information about number\n        of dropped upstream packets due to SAV failure.')
docsSecCmtsCertificate = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 9))
docsSecCmtsCertificateCertRevocationMethod = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("crl", 2), ("ocsp", 3), ("crlAndOcsp", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSecCmtsCertificateCertRevocationMethod.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCertificateCertRevocationMethod.setDescription("This attribute identifies which certificate revocation\n        method is to be used by the CMTS to verify the cable\n        modem certificate validity. The certificate revocation\n        methods include Certification Revocation\n        List (CRL) and Online Certificate Status Protocol\n        (OCSP).\n        The following options are available:\n        The option 'none' indicates that the CMTS does not attempt\n        to determine the revocation status of a certificate.\n\n        The option 'crl' indicates the CMTS uses a Certificate\n        Revocation List (CRL) as defined by the Url attribute\n        of the CmtsCertRevocationList object. When the\n        value of this attribute is changed to 'crl', it triggers\n        the CMTS to retrieve the CRL from the URL specified\n        by the Url attribute. If the value of this attribute\n        is 'crl' when the CMTS starts up, it triggers the CMTS\n        to retrieve the CRL from the URL specified by the Url attribute.\n\n        The option 'ocsp' indicates the CMTS uses the Online\n        Certificate Status Protocol (OCSP) as defined by the\n        Url attribute of the CmtsOnlineCertStatusProtocol\n        object.\n\n        The option 'crlAndOcsp' indicates the CMTS uses both\n        the CRL as defined by the Url attribute in the\n        CmtsCertRevocationList object and OCSP as defined by the Url\n        attribute in the CmtsOnlineCertStatusProtocol\n        object.\n        The CMTS persists the values of the CertRevocationMethod\n        attribute across reinitializations.")
docsSecCmtsCertRevocationList = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 10))
docsSecCmtsCertRevocationListUrl = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 10, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSecCmtsCertRevocationListUrl.setReference('DOCSIS 3.0 Security Specification\n         CM-SP-SECv3.0-I01-060804, BPI+ X.509 Certificate Profile\n         and Management Section.')
if mibBuilder.loadTexts: docsSecCmtsCertRevocationListUrl.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCertRevocationListUrl.setDescription('This attribute contains the URL from where the CMTS\n        will retrieve the CRL. When this attribute is set to\n        a URL value different from the current value, it triggers\n        the CMTS to retrieve the CRL from that URL. If the\n        value of this attribute is a zero-length string, the\n        CMTS does not attempt to retrieve the CRL.\n        The CMTS persists the value of Url across\n        reinitializations.')
docsSecCmtsCertRevocationListRefreshInterval = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 10, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 524160)).clone(10080)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSecCmtsCertRevocationListRefreshInterval.setReference('DOCSIS 3.0 Security Specification\n         CM-SP-SECv3.0-I01-060804, BPI+ X.509 Certificate Profile\n         and Management Section.')
if mibBuilder.loadTexts: docsSecCmtsCertRevocationListRefreshInterval.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCertRevocationListRefreshInterval.setDescription('This attribute contains the refresh interval for\n        the CMTS to retrieve the CRL (referred to in the Url attribute)\n        with the purpose of updating its Certificate\n        Revocation List. This attribute is meaningful if\n        the tbsCertList.nextUpdate attribute does not exist\n        in the last retrieved CRL, otherwise the value 0 is\n        returned.\n        The CMTS persists the value of RefreshInterval across\n        reinitializations.')
docsSecCmtsCertRevocationListLastUpdate = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 10, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSecCmtsCertRevocationListLastUpdate.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsCertRevocationListLastUpdate.setDescription('This attribute contains the last date and time when\n        the CRL was retrieved by the CMTS. This attribute returns\n        the initial EPOC time if the CRL has not being updated.\n        The CMTS persists the value of LastUpdate across\n        reinitializations.')
docsSecCmtsOnlineCertStatusProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 11))
docsSecCmtsOnlineCertStatusProtocolUrl = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 11, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSecCmtsOnlineCertStatusProtocolUrl.setReference('DOCSIS 3.0 Security Specification\n         CM-SP-SECv3.0-I01-060804, BPI+ X.509 Certificate Profile\n         and Management Section.\n         RFC 2560.')
if mibBuilder.loadTexts: docsSecCmtsOnlineCertStatusProtocolUrl.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsOnlineCertStatusProtocolUrl.setDescription('This attribute contains the URL string to retrieve\n        OCSP information. If the value of this attribute is\n        a zero-length string, the CMTS does not attempt to request\n        the status of a CM certificate.\n        The CMTS persists the value of Url across\n        reinitializations.')
docsSecCmtsOnlineCertStatusProtocolSignatureBypass = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 1, 11, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSecCmtsOnlineCertStatusProtocolSignatureBypass.setReference('DOCSIS 3.0 Security Specification\n         CM-SP-SECv3.0-I01-060804, BPI+ X.509 Certificate Profile\n         and Management Section.\n         RFC 2560.')
if mibBuilder.loadTexts: docsSecCmtsOnlineCertStatusProtocolSignatureBypass.setStatus('current')
if mibBuilder.loadTexts: docsSecCmtsOnlineCertStatusProtocolSignatureBypass.setDescription('This attribute enables or disables signature checking\n        on OCSP response messages.\n        The CMTS persists the value of SignatureBypass across\n        reinitializations.')
docsSecMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2))
docsSecMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2, 1))
docsSecMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2, 2))
docsSecCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2, 1, 1)).setObjects(("DOCS-SEC-MIB", "docsSecGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsSecCompliance = docsSecCompliance.setStatus('current')
if mibBuilder.loadTexts: docsSecCompliance.setDescription('The compliance statement for devices that implement the DOCSIS\n        Security MIB.')
docsSecGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 11, 2, 2, 1)).setObjects(("DOCS-SEC-MIB", "docsSecCmtsCertRevocationListUrl"), ("DOCS-SEC-MIB", "docsSecCmtsCertRevocationListRefreshInterval"), ("DOCS-SEC-MIB", "docsSecCmtsCertRevocationListLastUpdate"), ("DOCS-SEC-MIB", "docsSecCmtsOnlineCertStatusProtocolUrl"), ("DOCS-SEC-MIB", "docsSecCmtsOnlineCertStatusProtocolSignatureBypass"), ("DOCS-SEC-MIB", "docsSecCmtsServerCfgTftpOptions"), ("DOCS-SEC-MIB", "docsSecCmtsServerCfgConfigFileLearningEnable"), ("DOCS-SEC-MIB", "docsSecCmtsEncryptEncryptAlgPriority"), ("DOCS-SEC-MIB", "docsSecCmtsSavControlCmAuthEnable"), ("DOCS-SEC-MIB", "docsSecCmtsCmEaeExclusionMacAddr"), ("DOCS-SEC-MIB", "docsSecCmtsCmEaeExclusionMacAddrMask"), ("DOCS-SEC-MIB", "docsSecCmtsCmEaeExclusionRowStatus"), ("DOCS-SEC-MIB", "docsSecSavCmAuthGrpName"), ("DOCS-SEC-MIB", "docsSecSavCmAuthStaticPrefixListId"), ("DOCS-SEC-MIB", "docsSecSavCfgListPrefixAddrType"), ("DOCS-SEC-MIB", "docsSecSavCfgListPrefixAddr"), ("DOCS-SEC-MIB", "docsSecSavCfgListPrefixLen"), ("DOCS-SEC-MIB", "docsSecSavCfgListRowStatus"), ("DOCS-SEC-MIB", "docsSecSavStaticListPrefixAddrType"), ("DOCS-SEC-MIB", "docsSecSavStaticListPrefixAddr"), ("DOCS-SEC-MIB", "docsSecSavStaticListPrefixLen"), ("DOCS-SEC-MIB", "docsSecCmtsCmSavStatsSavDiscards"), ("DOCS-SEC-MIB", "docsSecCmtsCertificateCertRevocationMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsSecGroup = docsSecGroup.setStatus('current')
if mibBuilder.loadTexts: docsSecGroup.setDescription('Group of objects implemented in the CMTS.')
mibBuilder.exportSymbols("DOCS-SEC-MIB", docsSecCmtsCmEaeExclusionId=docsSecCmtsCmEaeExclusionId, docsSecSavStaticListId=docsSecSavStaticListId, docsSecSavCfgListRuleId=docsSecSavCfgListRuleId, docsSecCmtsCmSavStatsTable=docsSecCmtsCmSavStatsTable, docsSecCmtsCertRevocationListLastUpdate=docsSecCmtsCertRevocationListLastUpdate, docsSecCmtsSavControl=docsSecCmtsSavControl, docsSecSavCfgListName=docsSecSavCfgListName, docsSecCmtsCmEaeExclusionEntry=docsSecCmtsCmEaeExclusionEntry, docsSecCmtsCertRevocationListRefreshInterval=docsSecCmtsCertRevocationListRefreshInterval, docsSecSavCmAuthGrpName=docsSecSavCmAuthGrpName, docsSecMibGroups=docsSecMibGroups, docsSecCmtsCmEaeExclusionTable=docsSecCmtsCmEaeExclusionTable, docsSecSavCmAuthTable=docsSecSavCmAuthTable, docsSecSavCfgListPrefixLen=docsSecSavCfgListPrefixLen, docsSecSavStaticListPrefixAddr=docsSecSavStaticListPrefixAddr, docsSecSavCfgListEntry=docsSecSavCfgListEntry, docsSecSavCfgListRowStatus=docsSecSavCfgListRowStatus, docsSecCompliance=docsSecCompliance, docsSecCmtsCertificateCertRevocationMethod=docsSecCmtsCertificateCertRevocationMethod, docsSecCmtsCmEaeExclusionMacAddr=docsSecCmtsCmEaeExclusionMacAddr, docsSecCmtsCmEaeExclusionRowStatus=docsSecCmtsCmEaeExclusionRowStatus, docsSecCmtsCmSavStatsEntry=docsSecCmtsCmSavStatsEntry, docsSecSavStaticListRuleId=docsSecSavStaticListRuleId, docsSecCmtsCertRevocationList=docsSecCmtsCertRevocationList, docsSecMibObjects=docsSecMibObjects, docsSecSavCfgListTable=docsSecSavCfgListTable, docsSecCmtsServerCfg=docsSecCmtsServerCfg, docsSecSavStaticListEntry=docsSecSavStaticListEntry, docsSecMibCompliances=docsSecMibCompliances, docsSecMib=docsSecMib, docsSecSavStaticListTable=docsSecSavStaticListTable, docsSecCmtsEncrypt=docsSecCmtsEncrypt, docsSecMibConformance=docsSecMibConformance, docsSecCmtsCertRevocationListUrl=docsSecCmtsCertRevocationListUrl, docsSecSavCfgListPrefixAddrType=docsSecSavCfgListPrefixAddrType, docsSecCmtsSavControlCmAuthEnable=docsSecCmtsSavControlCmAuthEnable, docsSecSavStaticListPrefixAddrType=docsSecSavStaticListPrefixAddrType, docsSecSavStaticListPrefixLen=docsSecSavStaticListPrefixLen, docsSecSavCmAuthEntry=docsSecSavCmAuthEntry, docsSecCmtsEncryptEncryptAlgPriority=docsSecCmtsEncryptEncryptAlgPriority, docsSecCmtsServerCfgTftpOptions=docsSecCmtsServerCfgTftpOptions, docsSecCmtsCertificate=docsSecCmtsCertificate, docsSecGroup=docsSecGroup, docsSecCmtsOnlineCertStatusProtocolSignatureBypass=docsSecCmtsOnlineCertStatusProtocolSignatureBypass, docsSecSavCfgListPrefixAddr=docsSecSavCfgListPrefixAddr, docsSecSavCmAuthStaticPrefixListId=docsSecSavCmAuthStaticPrefixListId, docsSecCmtsCmSavStatsSavDiscards=docsSecCmtsCmSavStatsSavDiscards, PYSNMP_MODULE_ID=docsSecMib, docsSecCmtsServerCfgConfigFileLearningEnable=docsSecCmtsServerCfgConfigFileLearningEnable, docsSecCmtsOnlineCertStatusProtocolUrl=docsSecCmtsOnlineCertStatusProtocolUrl, docsSecCmtsCmEaeExclusionMacAddrMask=docsSecCmtsCmEaeExclusionMacAddrMask, docsSecCmtsOnlineCertStatusProtocol=docsSecCmtsOnlineCertStatusProtocol)
