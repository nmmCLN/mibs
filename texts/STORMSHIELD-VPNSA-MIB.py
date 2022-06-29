#
# PySNMP MIB module STORMSHIELD-VPNSA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-VPNSA-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:15:59 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, NotificationType, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, Integer32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "NotificationType", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "Integer32", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsVPN = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 1))
snsVPN.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsVPN.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsVPN.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsVPN.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsVPN.setContactInfo('Customer Support\n\n         22 rue du Gouverneur General Eboue\n         92130 Issy-les-Moulineaux\n         FRANCE\n\n         Tel: +33 (0)9 69 32 96 29\n         E-mail: support@stormshield.eu\n         http://www.stormshield.eu')
if mibBuilder.loadTexts: snsVPN.setDescription('stormshield VPN MIBS')
snsVPNSATable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1), )
if mibBuilder.loadTexts: snsVPNSATable.setStatus('current')
if mibBuilder.loadTexts: snsVPNSATable.setDescription('List of Security Association')
snsVPNSAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1), ).setIndexNames((0, "STORMSHIELD-VPNSA-MIB", "snsVPNSAIndex"))
if mibBuilder.loadTexts: snsVPNSAEntry.setStatus('current')
if mibBuilder.loadTexts: snsVPNSAEntry.setDescription('Each entry in the snsVPNSATable holds a set of parameters.')
snsVPNSAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNSAIndex.setStatus('current')
if mibBuilder.loadTexts: snsVPNSAIndex.setDescription('A unique value for phase one table.  Its value\n         ranges between 1 and 65535 and may not be contigous.\n         the index has no other meaning but a pure index')
snsVPNIPSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNIPSrc.setStatus('current')
if mibBuilder.loadTexts: snsVPNIPSrc.setDescription('IP source')
snsVPNIPDst = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNIPDst.setStatus('current')
if mibBuilder.loadTexts: snsVPNIPDst.setDescription('IP destination')
snsVPNType = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unspec", 0), ("unknown", 1), ("ah", 2), ("esp", 3), ("rsvp", 4), ("ospfv2", 5), ("ripv2", 6), ("mip", 7), ("ipcomp", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNType.setStatus('current')
if mibBuilder.loadTexts: snsVPNType.setDescription('Type')
snsVPNMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("any", 0), ("transport", 1), ("tunnel", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNMode.setStatus('current')
if mibBuilder.loadTexts: snsVPNMode.setDescription('Mode')
snsVPNSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNSpi.setStatus('current')
if mibBuilder.loadTexts: snsVPNSpi.setDescription('Secure property index')
snsVPNPeerSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNPeerSpi.setStatus('current')
if mibBuilder.loadTexts: snsVPNPeerSpi.setDescription('Secure property index of the peer')
snsVPNReqID = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNReqID.setStatus('current')
if mibBuilder.loadTexts: snsVPNReqID.setDescription('ReqID')
snsVPNEnc = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNEnc.setStatus('current')
if mibBuilder.loadTexts: snsVPNEnc.setDescription('Enc')
snsVPNAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 5, 6, 7, 249, 250, 251))).clone(namedValues=NamedValues(("none", 0), ("hmac-md5", 2), ("hmac-sha1", 3), ("hmac-sha256", 5), ("hmac-sha384", 6), ("hmac-sha512", 7), ("md5", 249), ("sha", 250), ("null", 251)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNAuth.setStatus('current')
if mibBuilder.loadTexts: snsVPNAuth.setDescription('Auth')
snsVPNState = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("larval", 0), ("mature", 1), ("dying", 2), ("dead", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNState.setStatus('current')
if mibBuilder.loadTexts: snsVPNState.setDescription('VPN State')
snsVPNLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNLifetime.setStatus('current')
if mibBuilder.loadTexts: snsVPNLifetime.setDescription('Lifetime')
snsVPNBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNBytes.setStatus('current')
if mibBuilder.loadTexts: snsVPNBytes.setDescription('Bytes')
snsVPNMaxLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNMaxLifetime.setStatus('current')
if mibBuilder.loadTexts: snsVPNMaxLifetime.setDescription('MaxLifetime')
snsVPNMaxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVPNMaxBytes.setStatus('current')
if mibBuilder.loadTexts: snsVPNMaxBytes.setDescription('MaxBytes')
mibBuilder.exportSymbols("STORMSHIELD-VPNSA-MIB", snsVPNAuth=snsVPNAuth, snsVPNPeerSpi=snsVPNPeerSpi, snsVPNReqID=snsVPNReqID, snsVPNBytes=snsVPNBytes, snsVPNEnc=snsVPNEnc, snsVPNMaxLifetime=snsVPNMaxLifetime, snsVPNSAIndex=snsVPNSAIndex, snsVPNState=snsVPNState, snsVPNLifetime=snsVPNLifetime, snsVPNIPDst=snsVPNIPDst, snsVPNSATable=snsVPNSATable, snsVPNMaxBytes=snsVPNMaxBytes, snsVPNIPSrc=snsVPNIPSrc, snsVPNType=snsVPNType, snsVPNMode=snsVPNMode, snsVPNSpi=snsVPNSpi, snsVPN=snsVPN, snsVPNSAEntry=snsVPNSAEntry, PYSNMP_MODULE_ID=snsVPN)
