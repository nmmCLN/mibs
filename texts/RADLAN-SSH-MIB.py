#
# PySNMP MIB module RADLAN-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SSH-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:32:54 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Counter64, Gauge32, ModuleIdentity, ObjectIdentity, MibIdentifier, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Counter64", "Gauge32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "iso", "Integer32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
rlSsh = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 78))
rlSsh.setRevisions(('2003-01-03 00:24', '2003-09-21 00:24',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSsh.setRevisionsDescriptions(('The second revision', 'Editorial changes.',))
if mibBuilder.loadTexts: rlSsh.setLastUpdated('200209300024Z')
if mibBuilder.loadTexts: rlSsh.setOrganization('Radlan Computer Communication Ltd.')
if mibBuilder.loadTexts: rlSsh.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlSsh.setDescription("The MIB module describes the private MIB for SSH supported\n               by Radlan's software and products.")
class RlSshPublicKeyAlgorithm(TextualConvention, Integer32):
    description = 'This textual convention describes the various possible public key\n         algorithms.  The key algorithm is used to select the PK to be generated\n         and is also used when viewing the public keys.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 999))
    namedValues = NamedValues(("rsa1", 0), ("rsa", 1), ("dsa", 2), ("none", 999))

class RlSshPublicKeyDigestFormat(TextualConvention, Integer32):
    description = 'This textual convention describes the format used to display the public\n         key fingerprint.  The hex format is the format used by PGP and OpenSSH.\n         The bubble-babble format is used by SSH.com software.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("hex", 0), ("bubbleBabble", 1))

rlSshMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlSshMibVersion.setDescription('The MIB version. The current version is 2')
rlSshServer = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 78, 2))
rlSshServerHostPublicKeyTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 2, 1), )
if mibBuilder.loadTexts: rlSshServerHostPublicKeyTable.setStatus('current')
if mibBuilder.loadTexts: rlSshServerHostPublicKeyTable.setDescription("This table contains the router's public key.  Each row in this table\n     contains a fragment of the key, in printable binhex format.  There may\n     be up to 160 characters in every fragment, and they are all combined\n     to form one key.  The key is generated by writing to\n     rlSshServerRegenerateHostKey.  To cause clients to connect to this router\n     without printing warning messages (and also prevent active\n     man-in-the-middle), the router's public key must printed out and inserted\n     into the client's authorized_keys file")
rlSshServerHostPublicKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 2, 1, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshServerHostPublicKeyAlgorithm"), (0, "RADLAN-SSH-MIB", "rlSshServerHostPublicKeyFragmentId"))
if mibBuilder.loadTexts: rlSshServerHostPublicKeyTableEntry.setStatus('current')
if mibBuilder.loadTexts: rlSshServerHostPublicKeyTableEntry.setDescription(' The row definition for this table.')
rlSshServerHostPublicKeyAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 1, 1, 1), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyAlgorithm.setStatus('current')
if mibBuilder.loadTexts: rlSshServerHostPublicKeyAlgorithm.setDescription('Identifies the type of public key to be displayed.')
rlSshServerHostPublicKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFragmentId.setStatus('current')
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFragmentId.setDescription('Identifies the index of this fragment in the final key.  All segments must\n     be combined to form one big key.')
rlSshServerHostPublicKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFragmentText.setStatus('current')
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFragmentText.setDescription("A part of the readable text entry for the server's public authorzation key.")
rlSshServerHostPublicKeyFingerprintTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 2, 2), )
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintTable.setStatus('current')
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintTable.setDescription("This table contains the fingerprint for the router's public key.")
rlSshServerHostPublicKeyFingerprintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 2, 2, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshServerHostPublicKeyFingerprintAlgorithm"), (0, "RADLAN-SSH-MIB", "rlSshServerHostPublicKeyFingerprintDigestFormat"))
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintTableEntry.setStatus('current')
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintTableEntry.setDescription(' The row definition for this table.')
rlSshServerHostPublicKeyFingerprintAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 2, 1, 1), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintAlgorithm.setStatus('current')
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintAlgorithm.setDescription('Identifies the type of public key to be displayed.')
rlSshServerHostPublicKeyFingerprintDigestFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 2, 1, 2), RlSshPublicKeyDigestFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintDigestFormat.setStatus('current')
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprintDigestFormat.setDescription('Format of the digest to be displayed (OpenSSH or SSH.com).')
rlSshServerHostPublicKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprint.setStatus('current')
if mibBuilder.loadTexts: rlSshServerHostPublicKeyFingerprint.setDescription("SECSH format fingerprint of the server's public key.  To prevent man in\n     the middle attacks, users should make sure the ssh Server's fingerprint,\n     as printed in the connection process, is similar to the one printed here.")
rlSshServerAuthorizedUsersPublicKeyTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 2, 3), )
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyTable.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyTable.setDescription("This table contains public keys for all users who are authorized to access\n    the router.  For a user to be able to log in using SSH, the user name must\n    appear in this table, and the user's public key must match the one found\n    here.")
rlSshServerAuthorizedUsersPublicKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 2, 3, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshServerAuthorizedUserName"), (0, "RADLAN-SSH-MIB", "rlSshServerAuthorizedUserPublicKeyFragmentId"))
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyTableEntry.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyTableEntry.setDescription(' The row definition for this table.')
rlSshServerAuthorizedUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserName.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUserName.setDescription('Name of the user who owns this public key.  Both the user name and the\n    key bytes must match before a user is authenticated using this key.')
rlSshServerAuthorizedUserPublicKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 3, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentId.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentId.setDescription('Identifies the index of this fragment in the final key.  All segments must\n     be combined to form one big key.')
rlSshServerAuthorizedUserPublicKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 3, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentText.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentText.setDescription("A part of the readable text entry for the user's public authorzation key.")
rlSshServerAuthorizedUserPublicKeyFragmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 3, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentStatus.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFragmentStatus.setDescription("Create or delete a fragment of the user's public key.\n    A user is deleted if it has no remaining fragments.")
rlSshServerAuthorizedUsersPublicKeyFingerprintTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 2, 5), )
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyFingerprintTable.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyFingerprintTable.setDescription("This table contains the fingerprints of the public keys for all users who\n     are authorized to access the router.\n     To prevent man in the middle attacks, users should make sure the\n     user's fingerprint, as printed in the connection process, is similar\n     to the one printed here.")
rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 2, 5, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshServerAuthorizedUserFingerprintName"), (0, "RADLAN-SSH-MIB", "rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat"))
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry.setDescription(' The row definition for this table.')
rlSshServerAuthorizedUserFingerprintName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserFingerprintName.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUserFingerprintName.setDescription('Name of the user who owns this public key.  Both the user name and the\n     key bytes must match before a user is authenticated using this key.')
rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 5, 1, 2), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm.setDescription('Identifies the type of public key to be displayed.')
rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 5, 1, 3), RlSshPublicKeyDigestFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat.setDescription('Format of the digest to be displayed (OpenSSH or SSH.com).')
rlSshServerAuthorizedUserPublicKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprint.setStatus('current')
if mibBuilder.loadTexts: rlSshServerAuthorizedUserPublicKeyFingerprint.setDescription("SECSH format fingerprint of the user's public key.  To prevent man in\n     the middle attacks, users should make sure their ssh fingerprint,\n     as printed in the connection process, is similar to the one printed here.")
rlSshServerSessionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 2, 6), )
if mibBuilder.loadTexts: rlSshServerSessionTable.setStatus('current')
if mibBuilder.loadTexts: rlSshServerSessionTable.setDescription('Each row in this table corresponds to an active SSH session with\n     the server')
rlSshServerSessionTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshServerSessionIdentifier"))
if mibBuilder.loadTexts: rlSshServerSessionTableEntry.setStatus('current')
if mibBuilder.loadTexts: rlSshServerSessionTableEntry.setDescription(' The row definition for this table.')
rlSshServerSessionIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionIdentifier.setStatus('current')
if mibBuilder.loadTexts: rlSshServerSessionIdentifier.setDescription('Identifies the connection to which this row corresponds.')
rlSshServerSessionPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionPeerAddress.setStatus('current')
if mibBuilder.loadTexts: rlSshServerSessionPeerAddress.setDescription('The network address of the remote host connected to the server.')
rlSshServerSessionPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionPeerPort.setStatus('current')
if mibBuilder.loadTexts: rlSshServerSessionPeerPort.setDescription('The source network port of the remote host connected to the server.')
rlSshServerSessionPeerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionPeerVersion.setStatus('current')
if mibBuilder.loadTexts: rlSshServerSessionPeerVersion.setDescription('The client version of the remote host connected to the server.')
rlSshServerSessionUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionUsername.setStatus('current')
if mibBuilder.loadTexts: rlSshServerSessionUsername.setDescription('SSH authenticated name of user connected to the server.')
rlSshServerSessionCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionCipher.setStatus('current')
if mibBuilder.loadTexts: rlSshServerSessionCipher.setDescription('Data encryption cipher used in this connection.')
rlSshServerSessionHMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 2, 6, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshServerSessionHMAC.setStatus('current')
if mibBuilder.loadTexts: rlSshServerSessionHMAC.setDescription('Message authentication code used in this connection.')
rlSshServerPort = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 2, 101), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerPort.setStatus('current')
if mibBuilder.loadTexts: rlSshServerPort.setDescription('Specifies the TCP port used by the SSH 2 Server to listen for incoming\n         connections.')
rlSshServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 2, 102), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerEnable.setStatus('current')
if mibBuilder.loadTexts: rlSshServerEnable.setDescription('Enables listening for incoming SSH2 connections on the port defined in\n        rlSshServerPort.')
rlSshServerEnablePublicKeyAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 2, 103), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerEnablePublicKeyAuthentication.setStatus('current')
if mibBuilder.loadTexts: rlSshServerEnablePublicKeyAuthentication.setDescription("If PK authentication is enabled, incoming SSH connections are\n        authenticated using public key authentication (using\n        rlSshServerAuthorizedUsersPublicKeyTable), before authenticating using\n        the router's standard AAA.  If disabled, SSH connections are only\n        authorized by the router's AAA component.")
rlSshServerRegenerateHostKey = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 2, 104), RlSshPublicKeyAlgorithm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshServerRegenerateHostKey.setStatus('current')
if mibBuilder.loadTexts: rlSshServerRegenerateHostKey.setDescription('Setting to a value other than none results in the Server (Host) Key\n        being regenerated.  The key size is host-specific.')
rlSshClient = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 78, 3))
rlSshClientUserName = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 3, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientUserName.setStatus('current')
if mibBuilder.loadTexts: rlSshClientUserName.setDescription('Specifies the default user name the ssh client will use when\n        authenticating to a remote server.')
rlSshClientRegenerateSelfKey = MibScalar((1, 3, 6, 1, 4, 1, 89, 78, 3, 2), RlSshPublicKeyAlgorithm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientRegenerateSelfKey.setStatus('current')
if mibBuilder.loadTexts: rlSshClientRegenerateSelfKey.setDescription('Setting to a value other than none results in the client self key\n        being regenerated.  The key size is host-specific.')
rlSshClientSelfPublicKeyTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 3, 3), )
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyTable.setStatus('current')
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyTable.setDescription("This table contains the router's client self public key.  Each row in\n    this table contains a fragment of the key, in printable binhex format.\n    There may be up to 160 characters in every fragment, and they are all\n    combined to form one key.  The key is generated by writing to\n    rlSshClientRegenerateSelfKey.  To cause clients to connect to this router\n    without printing warning messages (and also prevent active\n    man-in-the-middle), the router's public key must printed out and\n    inserted into the client's authorized_keys file")
rlSshClientSelfPublicKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 3, 3, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshClientSelfPublicKeyAlgorithm"), (0, "RADLAN-SSH-MIB", "rlSshClientSelfPublicKeyFragmentId"))
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyTableEntry.setStatus('current')
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyTableEntry.setDescription(' The row definition for this table.')
rlSshClientSelfPublicKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFragmentId.setStatus('current')
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFragmentId.setDescription('Identifies the index of this fragment in the final key.  All segments must\n     be combined to form one big key.')
rlSshClientSelfPublicKeyAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 3, 1, 2), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyAlgorithm.setStatus('current')
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyAlgorithm.setDescription('Identifies the type of public key to be displayed.')
rlSshClientSelfPublicKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 3, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFragmentText.setStatus('current')
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFragmentText.setDescription("A part of the readable text entry for the router's client public\n     authorization key.")
rlSshClientSelfPublicKeyFingerprintTable = MibTable((1, 3, 6, 1, 4, 1, 89, 78, 3, 4), )
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintTable.setStatus('current')
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintTable.setDescription("This table contains the fingerprint for the client's self key.  ")
rlSshClientSelfPublicKeyFingerprintTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 78, 3, 4, 1), ).setIndexNames((0, "RADLAN-SSH-MIB", "rlSshClientSelfPublicKeyFingerprintAlgorithm"), (0, "RADLAN-SSH-MIB", "rlSshClientSelfPublicKeyFingerprintDigestFormat"))
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintTableEntry.setStatus('current')
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintTableEntry.setDescription(' The row definition for this table.')
rlSshClientSelfPublicKeyFingerprintAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 4, 1, 1), RlSshPublicKeyAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintAlgorithm.setStatus('current')
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintAlgorithm.setDescription('Identifies the type of public key to be displayed.')
rlSshClientSelfPublicKeyFingerprintDigestFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 4, 1, 2), RlSshPublicKeyDigestFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintDigestFormat.setStatus('current')
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprintDigestFormat.setDescription('Format of the digest to be displayed (OpenSSH or SSH.com).')
rlSshClientSelfPublicKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 78, 3, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprint.setStatus('current')
if mibBuilder.loadTexts: rlSshClientSelfPublicKeyFingerprint.setDescription("SECSH format fingerprint of the client's self key.  To prevent man in\n     the middle attacks, users should make sure the ssh Server's fingerprint,\n     as printed in the connection process, is similar to the one printed here.")
mibBuilder.exportSymbols("RADLAN-SSH-MIB", rlSshServerSessionPeerAddress=rlSshServerSessionPeerAddress, rlSshServerSessionHMAC=rlSshServerSessionHMAC, rlSshServer=rlSshServer, rlSshServerSessionPeerPort=rlSshServerSessionPeerPort, rlSshClientSelfPublicKeyAlgorithm=rlSshClientSelfPublicKeyAlgorithm, rlSshServerHostPublicKeyFingerprintAlgorithm=rlSshServerHostPublicKeyFingerprintAlgorithm, PYSNMP_MODULE_ID=rlSsh, rlSshClientSelfPublicKeyFingerprint=rlSshClientSelfPublicKeyFingerprint, rlSshServerHostPublicKeyFingerprintTable=rlSshServerHostPublicKeyFingerprintTable, rlSshServerSessionIdentifier=rlSshServerSessionIdentifier, rlSshServerHostPublicKeyFragmentText=rlSshServerHostPublicKeyFragmentText, rlSshServerAuthorizedUsersPublicKeyTableEntry=rlSshServerAuthorizedUsersPublicKeyTableEntry, rlSshServerAuthorizedUserFingerprintName=rlSshServerAuthorizedUserFingerprintName, rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm=rlSshServerAuthorizedUserPublicKeyFingerprintAlgorithm, rlSshClientSelfPublicKeyFragmentId=rlSshClientSelfPublicKeyFragmentId, rlSshServerAuthorizedUserName=rlSshServerAuthorizedUserName, rlSshServerPort=rlSshServerPort, rlSshServerEnablePublicKeyAuthentication=rlSshServerEnablePublicKeyAuthentication, rlSshServerRegenerateHostKey=rlSshServerRegenerateHostKey, rlSshServerSessionTable=rlSshServerSessionTable, RlSshPublicKeyAlgorithm=RlSshPublicKeyAlgorithm, rlSshServerAuthorizedUsersPublicKeyTable=rlSshServerAuthorizedUsersPublicKeyTable, rlSshServerSessionCipher=rlSshServerSessionCipher, rlSshServerAuthorizedUserPublicKeyFragmentText=rlSshServerAuthorizedUserPublicKeyFragmentText, rlSshServerAuthorizedUsersPublicKeyFingerprintTable=rlSshServerAuthorizedUsersPublicKeyFingerprintTable, rlSshServerHostPublicKeyFragmentId=rlSshServerHostPublicKeyFragmentId, rlSshClientSelfPublicKeyTableEntry=rlSshClientSelfPublicKeyTableEntry, rlSshClientSelfPublicKeyFingerprintAlgorithm=rlSshClientSelfPublicKeyFingerprintAlgorithm, rlSshServerSessionPeerVersion=rlSshServerSessionPeerVersion, rlSshClientSelfPublicKeyTable=rlSshClientSelfPublicKeyTable, rlSshServerHostPublicKeyTableEntry=rlSshServerHostPublicKeyTableEntry, rlSsh=rlSsh, rlSshServerHostPublicKeyTable=rlSshServerHostPublicKeyTable, rlSshClientSelfPublicKeyFingerprintTable=rlSshClientSelfPublicKeyFingerprintTable, rlSshServerHostPublicKeyFingerprintDigestFormat=rlSshServerHostPublicKeyFingerprintDigestFormat, rlSshClientSelfPublicKeyFingerprintTableEntry=rlSshClientSelfPublicKeyFingerprintTableEntry, rlSshServerHostPublicKeyFingerprintTableEntry=rlSshServerHostPublicKeyFingerprintTableEntry, rlSshServerSessionTableEntry=rlSshServerSessionTableEntry, rlSshClientSelfPublicKeyFragmentText=rlSshClientSelfPublicKeyFragmentText, rlSshServerHostPublicKeyFingerprint=rlSshServerHostPublicKeyFingerprint, rlSshServerAuthorizedUserPublicKeyFragmentId=rlSshServerAuthorizedUserPublicKeyFragmentId, rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat=rlSshServerAuthorizedUserPublicKeyFingerprintDigestFormat, rlSshClientRegenerateSelfKey=rlSshClientRegenerateSelfKey, rlSshClientUserName=rlSshClientUserName, rlSshServerAuthorizedUserPublicKeyFingerprint=rlSshServerAuthorizedUserPublicKeyFingerprint, rlSshMibVersion=rlSshMibVersion, rlSshServerSessionUsername=rlSshServerSessionUsername, rlSshClient=rlSshClient, rlSshServerHostPublicKeyAlgorithm=rlSshServerHostPublicKeyAlgorithm, rlSshServerAuthorizedUserPublicKeyFragmentStatus=rlSshServerAuthorizedUserPublicKeyFragmentStatus, rlSshServerEnable=rlSshServerEnable, rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry=rlSshServerAuthorizedUsersPublicKeyFingerprintTableEntry, RlSshPublicKeyDigestFormat=RlSshPublicKeyDigestFormat, rlSshClientSelfPublicKeyFingerprintDigestFormat=rlSshClientSelfPublicKeyFingerprintDigestFormat)
