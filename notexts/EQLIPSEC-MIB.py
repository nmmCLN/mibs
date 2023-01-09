#
# PySNMP MIB module EQLIPSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLIPSEC-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:47 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlMemberIndex, = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlMemberIndex")
Unsigned64, = mibBuilder.importSymbols("EQLSTORAGEPOOL-MIB", "Unsigned64")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, Bits, ObjectIdentity, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, IpAddress, Gauge32, Integer32, Counter64, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "ObjectIdentity", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "IpAddress", "Gauge32", "Integer32", "Counter64", "Unsigned32", "enterprises")
RowPointer, DateAndTime, TimeStamp, StorageType, TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DateAndTime", "TimeStamp", "StorageType", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
eqlIpsecModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 22))
eqlIpsecModule.setRevisions(('2010-07-19 00:00',))
if mibBuilder.loadTexts: eqlIpsecModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlIpsecModule.setOrganization('EqualLogic Inc.')
eqlIpsecObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 22, 1))
eqlIpsecNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 22, 2))
eqlIpsecConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 22, 3))
class SnmpAdminString(TextualConvention, OctetString):
    status = 'current'
    displayHint = 't'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class InetPortNumber(TextualConvention, Unsigned32):
    reference = 'STD 6 (RFC 768), STD 7 (RFC 793) and RFC 2960'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IpsecAuthType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("presharedkey", 1), ("certificates", 2), ("manualkey", 3))

class IpsecIdType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("ipaddress", 2), ("userfqdn", 3), ("fqdn", 4), ("asn1dn", 5))

class IpsecEncType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("nullenc", 1), ("aes-cbc", 2), ("triple-des-cbc", 3))

eqlIpsecTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 22, 1, 1), )
if mibBuilder.loadTexts: eqlIpsecTable.setStatus('current')
eqlIpsecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 22, 1, 1, 1), ).setIndexNames((0, "EQLIPSEC-MIB", "eqlIpsecInstanceId"))
if mibBuilder.loadTexts: eqlIpsecEntry.setStatus('current')
eqlIpsecInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: eqlIpsecInstanceId.setStatus('current')
eqlIpsecEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlIpsecEnable.setStatus('current')
eqlIpsecRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecRowStatus.setStatus('current')
eqlIpsecPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2), )
if mibBuilder.loadTexts: eqlIpsecPolicyTable.setStatus('current')
eqlIpsecPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1), ).setIndexNames((0, "EQLIPSEC-MIB", "eqlIpsecPolicyInstanceId"))
if mibBuilder.loadTexts: eqlIpsecPolicyEntry.setStatus('current')
eqlIpsecPolicyInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: eqlIpsecPolicyInstanceId.setStatus('current')
eqlIpsecPolicyFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterName.setStatus('current')
eqlIpsecPolicyFilterIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 3), InetAddressType().clone('ipv6')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterIPVersion.setStatus('current')
eqlIpsecPolicyFilterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterAddress.setStatus('current')
eqlIpsecPolicyFilterNetmaskLen = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterNetmaskLen.setStatus('current')
eqlIpsecPolicyFilterLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterLocalAddress.setStatus('current')
eqlIpsecPolicyFilterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterPort.setStatus('current')
eqlIpsecPolicyFilterLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterLocalPort.setStatus('current')
eqlIpsecPolicyFilterProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterProtocol.setStatus('current')
eqlIpsecPolicyFilterPeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterPeerName.setStatus('current')
eqlIpsecPolicyFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ipsec", 1), ("pass", 2), ("drop", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterAction.setStatus('current')
eqlIpsecPolicyFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 2, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPolicyFilterRowStatus.setStatus('current')
eqlIpsecCertConfigTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 22, 1, 3), )
if mibBuilder.loadTexts: eqlIpsecCertConfigTable.setStatus('current')
eqlIpsecCertConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1), ).setIndexNames((0, "EQLIPSEC-MIB", "eqlIpsecCertInstanceId"))
if mibBuilder.loadTexts: eqlIpsecCertConfigEntry.setStatus('current')
eqlIpsecCertInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: eqlIpsecCertInstanceId.setStatus('current')
eqlIpsecCertName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertName.setStatus('current')
eqlIpsecCertFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertFileName.setStatus('current')
eqlIpsecCertType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("local-cert", 1), ("root-cert", 2), ("intermediate", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertType.setStatus('current')
eqlIpsecPrivKeyFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPrivKeyFileName.setStatus('current')
eqlIpsecCertPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertPassword.setStatus('current')
eqlIpsecCertRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertRowStatus.setStatus('current')
eqlIpsecPeerTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4), )
if mibBuilder.loadTexts: eqlIpsecPeerTable.setStatus('current')
eqlIpsecPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1), ).setIndexNames((0, "EQLIPSEC-MIB", "eqlIpsecPeerInstanceId"))
if mibBuilder.loadTexts: eqlIpsecPeerEntry.setStatus('current')
eqlIpsecPeerInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: eqlIpsecPeerInstanceId.setStatus('current')
eqlIpsecPeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerName.setStatus('current')
eqlIpsecPeerAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("presharedkey", 1), ("certificates", 2), ("manualkey", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerAuthType.setStatus('current')
eqlIpsecPeerPreSharedKey = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 130))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerPreSharedKey.setStatus('current')
eqlIpsecPeerCertIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("ipaddress", 2), ("userfqdn", 3), ("fqdn", 4), ("asn1dn", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlIpsecPeerCertIdType.setStatus('current')
eqlIpsecPeerCertIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlIpsecPeerCertIdValue.setStatus('current')
eqlIpsecPeerNullEnc = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerNullEnc.setStatus('current')
eqlIpsecPeerTunnelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerTunnelMode.setStatus('current')
eqlIpsecPeerTunnelAddressIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 9), InetAddressType().clone('ipv6')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerTunnelAddressIPVersion.setStatus('current')
eqlIpsecPeerTunnelAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 10), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerTunnelAddress.setStatus('current')
eqlIpsecPeerIkeV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerIkeV2.setStatus('current')
eqlIpsecPeerManualKeyEncAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 6, 7, 11, 12, 13, 250))).clone(namedValues=NamedValues(("none", 0), ("des-cbc", 2), ("triple-des-cbc", 3), ("cast128-cbc", 6), ("blowfish-cbc", 7), ("null-enc", 11), ("aes", 12), ("aes-ctr", 13), ("skipjack", 250)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerManualKeyEncAlg.setStatus('current')
eqlIpsecPeerManualKeyEncKeyOut = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 13), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerManualKeyEncKeyOut.setStatus('current')
eqlIpsecPeerManualKeyEncKeyIn = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 14), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerManualKeyEncKeyIn.setStatus('current')
eqlIpsecPeerManualKeyAuthAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("sha1", 1), ("sha256", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerManualKeyAuthAlg.setStatus('current')
eqlIpsecPeerManualKeyAuthKeyOut = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 16), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerManualKeyAuthKeyOut.setStatus('current')
eqlIpsecPeerManualKeyAuthKeyIn = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 17), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerManualKeyAuthKeyIn.setStatus('current')
eqlIpsecPeerManualKeySpiOut = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 18), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerManualKeySpiOut.setStatus('current')
eqlIpsecPeerManualKeySpiIn = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 19), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerManualKeySpiIn.setStatus('current')
eqlIpsecPeerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 4, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecPeerRowStatus.setStatus('current')
eqlIpsecCertDisplayTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5), )
if mibBuilder.loadTexts: eqlIpsecCertDisplayTable.setStatus('current')
eqlIpsecCertDisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1), ).setIndexNames((0, "EQLIPSEC-MIB", "eqlIpsecCertInstanceId"))
if mibBuilder.loadTexts: eqlIpsecCertDisplayEntry.setStatus('current')
eqlIpsecCertDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplayName.setStatus('current')
eqlIpsecCertDisplayIssuedToDName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplayIssuedToDName.setStatus('current')
eqlIpsecCertDisplaySerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplaySerialNumber.setStatus('current')
eqlIpsecCertDisplayIssuedByDName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplayIssuedByDName.setStatus('current')
eqlIpsecCertDisplayIssuedOn = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplayIssuedOn.setStatus('current')
eqlIpsecCertDisplayExpiresOn = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplayExpiresOn.setStatus('current')
eqlIpsecCertDisplaySha1Fingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplaySha1Fingerprint.setStatus('current')
eqlIpsecCertDisplayMd5Fingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplayMd5Fingerprint.setStatus('current')
eqlIpsecCertDisplayLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("local-cert", 1), ("root-cert", 2), ("intermediate", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplayLocal.setStatus('current')
eqlIpsecCertDisplayFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("x509", 1), ("pkcs12", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplayFormat.setStatus('current')
eqlIpsecCertDisplaySubAltName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 5, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecCertDisplaySubAltName.setStatus('current')
eqlIpsecSecAssocTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6), )
if mibBuilder.loadTexts: eqlIpsecSecAssocTable.setStatus('current')
eqlIpsecSecAssocEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLIPSEC-MIB", "eqlIpsecSecAssocInstanceIdHigh"), (0, "EQLIPSEC-MIB", "eqlIpsecSecAssocInstanceIdLow"))
if mibBuilder.loadTexts: eqlIpsecSecAssocEntry.setStatus('current')
eqlIpsecSecAssocInstanceIdHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlIpsecSecAssocInstanceIdHigh.setStatus('current')
eqlIpsecSecAssocInstanceIdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 2), Unsigned32())
if mibBuilder.loadTexts: eqlIpsecSecAssocInstanceIdLow.setStatus('current')
eqlIpsecSecAssocSrcAddressIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecSecAssocSrcAddressIPVersion.setStatus('current')
eqlIpsecSecAssocSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecSecAssocSrcAddress.setStatus('current')
eqlIpsecSecAssocDstAddressIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecSecAssocDstAddressIPVersion.setStatus('current')
eqlIpsecSecAssocDstAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecSecAssocDstAddress.setStatus('current')
eqlIpsecSecAssocEncAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 6, 7, 11, 12, 13, 250))).clone(namedValues=NamedValues(("none", 0), ("des-cbc", 2), ("triple-des-cbc", 3), ("cast128-cbc", 6), ("blowfish-cbc", 7), ("null-enc", 11), ("aes", 12), ("aes-ctr", 13), ("skipjack", 250)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecSecAssocEncAlg.setStatus('current')
eqlIpsecSecAssocAuthAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 5, 6, 7, 8, 9, 249, 250, 251, 252))).clone(namedValues=NamedValues(("none", 0), ("md5-hmac", 2), ("sha1-hmac", 3), ("sha2-256", 5), ("sha2-384", 6), ("sha2-512", 7), ("ripemd160-hmac", 8), ("aes-xcbc-mac", 9), ("md5", 249), ("sha", 250), ("null", 251), ("tcp-md5", 252)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecSecAssocAuthAlg.setStatus('current')
eqlIpsecSecAssocSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecSecAssocSpi.setStatus('current')
eqlIpsecSecAssocEncKey = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecSecAssocEncKey.setStatus('current')
eqlIpsecSecAssocAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecSecAssocAuthKey.setStatus('current')
eqlIpsecSecAssocManual = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 6, 1, 12), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecSecAssocManual.setStatus('current')
eqlIpsecStaleSecAssocDeleteTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 22, 1, 7), )
if mibBuilder.loadTexts: eqlIpsecStaleSecAssocDeleteTable.setStatus('current')
eqlIpsecStaleSecAssocDeleteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 22, 1, 7, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLIPSEC-MIB", "eqlIpsecStaleSecAssocDeleteInstanceId"))
if mibBuilder.loadTexts: eqlIpsecStaleSecAssocDeleteEntry.setStatus('current')
eqlIpsecStaleSecAssocDeleteInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 7, 1, 1), Integer32())
if mibBuilder.loadTexts: eqlIpsecStaleSecAssocDeleteInstanceId.setStatus('current')
eqlIpsecStaleSecAssocDeleteDestAddressIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 7, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecStaleSecAssocDeleteDestAddressIPVersion.setStatus('current')
eqlIpsecStaleSecAssocDeleteDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 7, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecStaleSecAssocDeleteDestAddress.setStatus('current')
eqlIpsecStaleSecAssocDeleteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 22, 1, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlIpsecStaleSecAssocDeleteRowStatus.setStatus('current')
mibBuilder.exportSymbols("EQLIPSEC-MIB", eqlIpsecPeerManualKeyAuthKeyOut=eqlIpsecPeerManualKeyAuthKeyOut, eqlIpsecStaleSecAssocDeleteDestAddressIPVersion=eqlIpsecStaleSecAssocDeleteDestAddressIPVersion, eqlIpsecObjects=eqlIpsecObjects, eqlIpsecPolicyFilterName=eqlIpsecPolicyFilterName, eqlIpsecPeerNullEnc=eqlIpsecPeerNullEnc, eqlIpsecPolicyEntry=eqlIpsecPolicyEntry, eqlIpsecCertDisplayName=eqlIpsecCertDisplayName, eqlIpsecCertConfigEntry=eqlIpsecCertConfigEntry, eqlIpsecNotifications=eqlIpsecNotifications, eqlIpsecPeerManualKeySpiOut=eqlIpsecPeerManualKeySpiOut, eqlIpsecPeerInstanceId=eqlIpsecPeerInstanceId, eqlIpsecSecAssocEncAlg=eqlIpsecSecAssocEncAlg, eqlIpsecPeerCertIdType=eqlIpsecPeerCertIdType, eqlIpsecEntry=eqlIpsecEntry, IpsecAuthType=IpsecAuthType, eqlIpsecEnable=eqlIpsecEnable, eqlIpsecCertDisplayMd5Fingerprint=eqlIpsecCertDisplayMd5Fingerprint, eqlIpsecModule=eqlIpsecModule, eqlIpsecPolicyFilterNetmaskLen=eqlIpsecPolicyFilterNetmaskLen, eqlIpsecCertDisplayTable=eqlIpsecCertDisplayTable, eqlIpsecStaleSecAssocDeleteEntry=eqlIpsecStaleSecAssocDeleteEntry, eqlIpsecPolicyFilterRowStatus=eqlIpsecPolicyFilterRowStatus, eqlIpsecInstanceId=eqlIpsecInstanceId, IpsecIdType=IpsecIdType, eqlIpsecPeerIkeV2=eqlIpsecPeerIkeV2, eqlIpsecSecAssocInstanceIdLow=eqlIpsecSecAssocInstanceIdLow, eqlIpsecSecAssocTable=eqlIpsecSecAssocTable, eqlIpsecCertConfigTable=eqlIpsecCertConfigTable, eqlIpsecPolicyFilterPeerName=eqlIpsecPolicyFilterPeerName, eqlIpsecPeerEntry=eqlIpsecPeerEntry, eqlIpsecPeerName=eqlIpsecPeerName, eqlIpsecRowStatus=eqlIpsecRowStatus, eqlIpsecStaleSecAssocDeleteRowStatus=eqlIpsecStaleSecAssocDeleteRowStatus, PYSNMP_MODULE_ID=eqlIpsecModule, eqlIpsecStaleSecAssocDeleteTable=eqlIpsecStaleSecAssocDeleteTable, eqlIpsecCertFileName=eqlIpsecCertFileName, eqlIpsecPeerRowStatus=eqlIpsecPeerRowStatus, eqlIpsecSecAssocSrcAddress=eqlIpsecSecAssocSrcAddress, eqlIpsecCertDisplayExpiresOn=eqlIpsecCertDisplayExpiresOn, IpsecEncType=IpsecEncType, eqlIpsecPeerManualKeyAuthAlg=eqlIpsecPeerManualKeyAuthAlg, eqlIpsecSecAssocDstAddress=eqlIpsecSecAssocDstAddress, eqlIpsecPeerManualKeySpiIn=eqlIpsecPeerManualKeySpiIn, SnmpAdminString=SnmpAdminString, eqlIpsecSecAssocSpi=eqlIpsecSecAssocSpi, eqlIpsecPeerManualKeyAuthKeyIn=eqlIpsecPeerManualKeyAuthKeyIn, eqlIpsecPeerAuthType=eqlIpsecPeerAuthType, eqlIpsecCertName=eqlIpsecCertName, eqlIpsecCertDisplayIssuedOn=eqlIpsecCertDisplayIssuedOn, eqlIpsecCertDisplaySubAltName=eqlIpsecCertDisplaySubAltName, eqlIpsecStaleSecAssocDeleteInstanceId=eqlIpsecStaleSecAssocDeleteInstanceId, eqlIpsecStaleSecAssocDeleteDestAddress=eqlIpsecStaleSecAssocDeleteDestAddress, eqlIpsecSecAssocAuthAlg=eqlIpsecSecAssocAuthAlg, eqlIpsecSecAssocEntry=eqlIpsecSecAssocEntry, eqlIpsecPolicyFilterLocalPort=eqlIpsecPolicyFilterLocalPort, eqlIpsecPolicyFilterIPVersion=eqlIpsecPolicyFilterIPVersion, eqlIpsecConformance=eqlIpsecConformance, eqlIpsecCertRowStatus=eqlIpsecCertRowStatus, eqlIpsecPeerPreSharedKey=eqlIpsecPeerPreSharedKey, eqlIpsecPeerManualKeyEncAlg=eqlIpsecPeerManualKeyEncAlg, eqlIpsecCertType=eqlIpsecCertType, eqlIpsecSecAssocEncKey=eqlIpsecSecAssocEncKey, eqlIpsecPolicyFilterPort=eqlIpsecPolicyFilterPort, eqlIpsecPolicyFilterLocalAddress=eqlIpsecPolicyFilterLocalAddress, eqlIpsecCertDisplayEntry=eqlIpsecCertDisplayEntry, eqlIpsecPolicyInstanceId=eqlIpsecPolicyInstanceId, eqlIpsecPeerTunnelAddress=eqlIpsecPeerTunnelAddress, eqlIpsecCertDisplaySerialNumber=eqlIpsecCertDisplaySerialNumber, eqlIpsecPolicyFilterAddress=eqlIpsecPolicyFilterAddress, eqlIpsecTable=eqlIpsecTable, eqlIpsecCertDisplayIssuedToDName=eqlIpsecCertDisplayIssuedToDName, eqlIpsecCertDisplaySha1Fingerprint=eqlIpsecCertDisplaySha1Fingerprint, eqlIpsecSecAssocDstAddressIPVersion=eqlIpsecSecAssocDstAddressIPVersion, eqlIpsecPeerTable=eqlIpsecPeerTable, eqlIpsecPolicyFilterAction=eqlIpsecPolicyFilterAction, eqlIpsecSecAssocInstanceIdHigh=eqlIpsecSecAssocInstanceIdHigh, eqlIpsecCertDisplayFormat=eqlIpsecCertDisplayFormat, eqlIpsecCertInstanceId=eqlIpsecCertInstanceId, eqlIpsecCertDisplayIssuedByDName=eqlIpsecCertDisplayIssuedByDName, eqlIpsecPeerCertIdValue=eqlIpsecPeerCertIdValue, eqlIpsecSecAssocSrcAddressIPVersion=eqlIpsecSecAssocSrcAddressIPVersion, eqlIpsecPolicyFilterProtocol=eqlIpsecPolicyFilterProtocol, eqlIpsecSecAssocManual=eqlIpsecSecAssocManual, eqlIpsecPeerManualKeyEncKeyOut=eqlIpsecPeerManualKeyEncKeyOut, eqlIpsecPeerTunnelMode=eqlIpsecPeerTunnelMode, eqlIpsecCertDisplayLocal=eqlIpsecCertDisplayLocal, eqlIpsecPolicyTable=eqlIpsecPolicyTable, eqlIpsecPrivKeyFileName=eqlIpsecPrivKeyFileName, eqlIpsecSecAssocAuthKey=eqlIpsecSecAssocAuthKey, eqlIpsecPeerManualKeyEncKeyIn=eqlIpsecPeerManualKeyEncKeyIn, eqlIpsecPeerTunnelAddressIPVersion=eqlIpsecPeerTunnelAddressIPVersion, InetPortNumber=InetPortNumber, eqlIpsecCertPassword=eqlIpsecCertPassword)
