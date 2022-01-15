#
# PySNMP MIB module SL-SECU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-SECU-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:45 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Gauge32, transmission, Counter64, iso, Integer32, NotificationType, Bits, Counter32, ModuleIdentity, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Gauge32", "transmission", "Counter64", "iso", "Integer32", "NotificationType", "Bits", "Counter32", "ModuleIdentity", "ObjectIdentity", "Unsigned32")
RowStatus, TruthValue, TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString", "DateAndTime")
slSecuMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24))
if mibBuilder.loadTexts: slSecuMib.setLastUpdated('201105170000Z')
if mibBuilder.loadTexts: slSecuMib.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slSecuMib.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slSecuMib.setDescription('This security module. This mib is used to configure the firewall.')
class SlSecuType(TextualConvention, Integer32):
    description = 'The security protocol types:\n        \tTelnet \t- CLI\n        \tSSH  \t- Secured Telnet\n        \tHTTP \t- Hyper Text\n        \tHTTPS\t- Secured HTTP\n        \tICMP\t- Ping\n        \tSNMP\t- Simple Network Management (only 161 is supported)\n        \tFTP\t\t- File Transfer\n        \tTFTP\t- Trivial FTP\n        \tTL1\t\t- TL1 over Telnet\n        \tTL1SSH  - TL1 over SSH\n        \tWL\t\t- White list (port number is 0)\n        \tSNMPOVERTCP - SNMP over TCP\n        \tSFTP\t- Client side'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("telnet", 1), ("ssh", 2), ("http", 3), ("https", 4), ("icmp", 5), ("snmp", 6), ("ftp", 7), ("tftp", 8), ("tl1", 9), ("tl1ssh", 10), ("wl", 11), ("snmpovertcp", 12), ("sftp", 13))

slSecuGen = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 1))
slSecuSelect = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2))
slSecuWl = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3))
slSecuEncryption = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4))
slSecuFirewallEnable = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuFirewallEnable.setStatus('current')
if mibBuilder.loadTexts: slSecuFirewallEnable.setDescription('General Enable/Disable of the firewall operation.')
slSecuSelectTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1), )
if mibBuilder.loadTexts: slSecuSelectTable.setStatus('current')
if mibBuilder.loadTexts: slSecuSelectTable.setDescription('The security protocol selection table.')
slSecuSelectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1), ).setIndexNames((0, "SL-SECU-MIB", "slSecuSelectType"))
if mibBuilder.loadTexts: slSecuSelectEntry.setStatus('current')
if mibBuilder.loadTexts: slSecuSelectEntry.setDescription('An entry in the security selection table.')
slSecuSelectType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1, 1), SlSecuType())
if mibBuilder.loadTexts: slSecuSelectType.setStatus('current')
if mibBuilder.loadTexts: slSecuSelectType.setDescription('The secutity protocol type')
slSecuSelectPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuSelectPort.setStatus('current')
if mibBuilder.loadTexts: slSecuSelectPort.setDescription('The corresponding port number of the protocol.\n       Port number 0 is used when not applicable/available.')
slSecuSelectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuSelectEnable.setStatus('current')
if mibBuilder.loadTexts: slSecuSelectEnable.setDescription('True - Enables the firewall for the corresponding protocol.\n       False - Dsables the firewall for the corresponding protocol.\n       When enabled the firewall blocks the protocol.')
slSecuWlTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1), )
if mibBuilder.loadTexts: slSecuWlTable.setStatus('current')
if mibBuilder.loadTexts: slSecuWlTable.setDescription('This white list table.')
slSecuWlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1), ).setIndexNames((0, "SL-SECU-MIB", "slSecuWlIp"))
if mibBuilder.loadTexts: slSecuWlEntry.setStatus('current')
if mibBuilder.loadTexts: slSecuWlEntry.setDescription('A particular IP address.')
slSecuWlIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuWlIp.setStatus('current')
if mibBuilder.loadTexts: slSecuWlIp.setDescription('The IP address to allow')
slSecuWlMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuWlMask.setStatus('current')
if mibBuilder.loadTexts: slSecuWlMask.setDescription('Indicate the mask to be logical-ANDed with the\n       destination  address  before  being compared to\n       the value  in  the  slSecuWlIp field.')
slSecuWlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: slSecuWlStatus.setStatus('current')
if mibBuilder.loadTexts: slSecuWlStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
slSecuEncryptionTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1), )
if mibBuilder.loadTexts: slSecuEncryptionTable.setStatus('current')
if mibBuilder.loadTexts: slSecuEncryptionTable.setDescription('The encryption table. This table has an entry per transponder.')
slSecuEncryptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1), ).setIndexNames((0, "SL-SECU-MIB", "slSecuEncryptionIfIndex"))
if mibBuilder.loadTexts: slSecuEncryptionEntry.setStatus('current')
if mibBuilder.loadTexts: slSecuEncryptionEntry.setDescription('This entry is used to control the necryption per transponder.')
slSecuEncryptionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuEncryptionIfIndex.setStatus('current')
if mibBuilder.loadTexts: slSecuEncryptionIfIndex.setDescription('The Interface Index of the uplink port.')
slSecuEncryptionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuEncryptionEnable.setStatus('current')
if mibBuilder.loadTexts: slSecuEncryptionEnable.setDescription('Enable/Disable the encryption on this uplink.')
slSecuEncryptionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("init", 1), ("exchange", 2), ("kdf", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuEncryptionStatus.setStatus('current')
if mibBuilder.loadTexts: slSecuEncryptionStatus.setDescription('The state of the encryption finite state machine.')
slSecuEncryptionForceInit = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuEncryptionForceInit.setStatus('current')
if mibBuilder.loadTexts: slSecuEncryptionForceInit.setDescription('Writing this valiable forces init to the encryption state machine.')
slSecuEncryptionPreShared = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuEncryptionPreShared.setStatus('current')
if mibBuilder.loadTexts: slSecuEncryptionPreShared.setDescription('The pre-shared secret. \n\t\tEither the pre-shared key, or the shared secret to avoid Mitm when using DH public key exchange.')
slSecuEncryptionKeyExchangePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuEncryptionKeyExchangePeriod.setStatus('current')
if mibBuilder.loadTexts: slSecuEncryptionKeyExchangePeriod.setDescription('The Key Exchage Period, specified in minutes.\n\t\tThe value 0 means to perform the key exchange only once at link establishment.')
slSecuEncryptionLock = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slSecuEncryptionLock.setStatus('current')
if mibBuilder.loadTexts: slSecuEncryptionLock.setDescription('Lock/Unlock the encrypted service for this uplink.')
slSecuEncryptionProtectedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 24, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("init", 1), ("exchange", 2), ("kdf", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slSecuEncryptionProtectedStatus.setStatus('current')
if mibBuilder.loadTexts: slSecuEncryptionProtectedStatus.setDescription('The protected port state of the encryption finite state machine.')
mibBuilder.exportSymbols("SL-SECU-MIB", slSecuEncryptionForceInit=slSecuEncryptionForceInit, slSecuFirewallEnable=slSecuFirewallEnable, slSecuEncryptionEnable=slSecuEncryptionEnable, slSecuWlStatus=slSecuWlStatus, slSecuSelectPort=slSecuSelectPort, slSecuWlMask=slSecuWlMask, slSecuEncryptionLock=slSecuEncryptionLock, slSecuEncryptionEntry=slSecuEncryptionEntry, slSecuEncryption=slSecuEncryption, slSecuWl=slSecuWl, slSecuWlTable=slSecuWlTable, PYSNMP_MODULE_ID=slSecuMib, slSecuMib=slSecuMib, SlSecuType=SlSecuType, slSecuWlEntry=slSecuWlEntry, slSecuGen=slSecuGen, slSecuSelectEntry=slSecuSelectEntry, slSecuEncryptionKeyExchangePeriod=slSecuEncryptionKeyExchangePeriod, slSecuSelect=slSecuSelect, slSecuEncryptionTable=slSecuEncryptionTable, slSecuSelectType=slSecuSelectType, slSecuEncryptionIfIndex=slSecuEncryptionIfIndex, slSecuEncryptionStatus=slSecuEncryptionStatus, slSecuEncryptionProtectedStatus=slSecuEncryptionProtectedStatus, slSecuEncryptionPreShared=slSecuEncryptionPreShared, slSecuSelectEnable=slSecuSelectEnable, slSecuWlIp=slSecuWlIp, slSecuSelectTable=slSecuSelectTable)
