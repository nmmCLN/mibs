#
# PySNMP MIB module STORMSHIELD-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-IF-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:28:41 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, Unsigned32, TimeTicks, Bits, Counter32, MibIdentifier, Gauge32, ObjectIdentity, Counter64, IpAddress, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Unsigned32", "TimeTicks", "Bits", "Counter32", "MibIdentifier", "Gauge32", "ObjectIdentity", "Counter64", "IpAddress", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsif = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 4))
snsif.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsif.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsif.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsif.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsif.setContactInfo('Customer Support\n\n         22 rue du Gouverneur General Eboue\n         92130 Issy-les-Moulineaux\n         FRANCE\n\n         Tel: +33 (0)9 69 32 96 29\n         E-mail: support@stormshield.eu\n         http://www.stormshield.eu')
if mibBuilder.loadTexts: snsif.setDescription('stormshield Interface MIBS')
snsifTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1), )
if mibBuilder.loadTexts: snsifTable.setStatus('current')
if mibBuilder.loadTexts: snsifTable.setDescription('List of interfaces')
snsifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1), ).setIndexNames((0, "STORMSHIELD-IF-MIB", "snsifIndex"))
if mibBuilder.loadTexts: snsifEntry.setStatus('current')
if mibBuilder.loadTexts: snsifEntry.setDescription('Each entry in the snsifTable holds a set of information.')
snsifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifIndex.setStatus('current')
if mibBuilder.loadTexts: snsifIndex.setDescription('A unique value for the table. Its value\n      ranges between 1 and 65535 and may not be contigous.\n      the index has no other meaning but a pure index')
snsifUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifUserName.setStatus('current')
if mibBuilder.loadTexts: snsifUserName.setDescription('User interface name')
snsifName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifName.setStatus('current')
if mibBuilder.loadTexts: snsifName.setDescription('System interface name')
snsifAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifAddr.setStatus('current')
if mibBuilder.loadTexts: snsifAddr.setDescription('Interface address')
snsifMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifMask.setStatus('current')
if mibBuilder.loadTexts: snsifMask.setDescription('Interface mask')
snsifType = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifType.setStatus('current')
if mibBuilder.loadTexts: snsifType.setDescription('Interface type')
snsifColor = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifColor.setStatus('current')
if mibBuilder.loadTexts: snsifColor.setDescription('')
snsifMacThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifMacThroughput.setStatus('current')
if mibBuilder.loadTexts: snsifMacThroughput.setDescription(' ')
snsifCurThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifCurThroughput.setStatus('current')
if mibBuilder.loadTexts: snsifCurThroughput.setDescription('incoming + outgoing current throughput in B/s ')
snsifMaxThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifMaxThroughput.setStatus('current')
if mibBuilder.loadTexts: snsifMaxThroughput.setDescription('incoming + outgoing maximum throughput in B/s')
snsifPktAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifPktAccepted.setStatus('current')
if mibBuilder.loadTexts: snsifPktAccepted.setDescription('number of accepted packets')
snsifPktBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifPktBlocked.setStatus('current')
if mibBuilder.loadTexts: snsifPktBlocked.setDescription('number of packets that have been blocked')
snsifPktFragmented = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifPktFragmented.setStatus('current')
if mibBuilder.loadTexts: snsifPktFragmented.setDescription('number of fragmented packets')
snsifPktTcp = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifPktTcp.setStatus('current')
if mibBuilder.loadTexts: snsifPktTcp.setDescription('Number of TCP packets forwarded')
snsifPktUdp = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifPktUdp.setStatus('current')
if mibBuilder.loadTexts: snsifPktUdp.setDescription('Number of UDP packets forwarded')
snsifPktIcmp = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifPktIcmp.setStatus('current')
if mibBuilder.loadTexts: snsifPktIcmp.setDescription('Number of ICMP packets forwarded')
snsifTotalBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifTotalBytes.setStatus('current')
if mibBuilder.loadTexts: snsifTotalBytes.setDescription('data bytes forwarded')
snsifTcpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifTcpBytes.setStatus('current')
if mibBuilder.loadTexts: snsifTcpBytes.setDescription('incoming + outgoing TCP data bytes')
snsifUdpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifUdpBytes.setStatus('current')
if mibBuilder.loadTexts: snsifUdpBytes.setDescription('incoming + outgoing UDP data bytes')
snsifIcmpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifIcmpBytes.setStatus('current')
if mibBuilder.loadTexts: snsifIcmpBytes.setDescription('incoming + outgoing ICMP data bytes')
snsifTcpConn = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifTcpConn.setStatus('current')
if mibBuilder.loadTexts: snsifTcpConn.setDescription('TCP connection established')
snsifUdpConn = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifUdpConn.setStatus('current')
if mibBuilder.loadTexts: snsifUdpConn.setDescription('UDP connection established')
snsifTcpConnCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifTcpConnCount.setStatus('current')
if mibBuilder.loadTexts: snsifTcpConnCount.setDescription('current TCP connection count')
snsifUdpConnCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifUdpConnCount.setStatus('current')
if mibBuilder.loadTexts: snsifUdpConnCount.setDescription('current UCP connection count')
snsifInCurThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifInCurThroughput.setStatus('current')
if mibBuilder.loadTexts: snsifInCurThroughput.setDescription('Incoming Current throughput in B/s ')
snsifOutCurThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifOutCurThroughput.setStatus('current')
if mibBuilder.loadTexts: snsifOutCurThroughput.setDescription('Outgoing Current throughput in B/s ')
snsifInMaxThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifInMaxThroughput.setStatus('current')
if mibBuilder.loadTexts: snsifInMaxThroughput.setDescription('Incoming maximum throughput in B/s')
snsifOutMaxThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifOutMaxThroughput.setStatus('current')
if mibBuilder.loadTexts: snsifOutMaxThroughput.setDescription('Outgoing maximum throughput in B/s')
snsifInTotalBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifInTotalBytes.setStatus('current')
if mibBuilder.loadTexts: snsifInTotalBytes.setDescription('Incoming data bytes')
snsifOutTotalBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifOutTotalBytes.setStatus('current')
if mibBuilder.loadTexts: snsifOutTotalBytes.setDescription('Outgoing data bytes')
snsifInTcpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifInTcpBytes.setStatus('current')
if mibBuilder.loadTexts: snsifInTcpBytes.setDescription('Incoming TCP data bytes')
snsifOutTcpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifOutTcpBytes.setStatus('current')
if mibBuilder.loadTexts: snsifOutTcpBytes.setDescription('Outgoing TCP data bytes')
snsifInUdpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifInUdpBytes.setStatus('current')
if mibBuilder.loadTexts: snsifInUdpBytes.setDescription('Incoming UDP data bytes')
snsifOutUdpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifOutUdpBytes.setStatus('current')
if mibBuilder.loadTexts: snsifOutUdpBytes.setDescription('Outgoing UDP data bytes')
snsifInIcmpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifInIcmpBytes.setStatus('current')
if mibBuilder.loadTexts: snsifInIcmpBytes.setDescription('Incoming ICMP data bytes')
snsifOutIcmpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifOutIcmpBytes.setStatus('current')
if mibBuilder.loadTexts: snsifOutIcmpBytes.setDescription('Outgoing ICMP data bytes')
snsifProtected = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifProtected.setStatus('current')
if mibBuilder.loadTexts: snsifProtected.setDescription('Is interface protected ?')
snsifDrvName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 38), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsifDrvName.setStatus('current')
if mibBuilder.loadTexts: snsifDrvName.setDescription('Driver interface name')
mibBuilder.exportSymbols("STORMSHIELD-IF-MIB", snsifOutUdpBytes=snsifOutUdpBytes, snsifPktUdp=snsifPktUdp, snsifInTcpBytes=snsifInTcpBytes, snsifUdpConn=snsifUdpConn, snsifOutTotalBytes=snsifOutTotalBytes, snsifMaxThroughput=snsifMaxThroughput, snsifIndex=snsifIndex, snsifPktTcp=snsifPktTcp, snsifPktIcmp=snsifPktIcmp, snsifAddr=snsifAddr, snsifMacThroughput=snsifMacThroughput, snsifColor=snsifColor, snsifUdpConnCount=snsifUdpConnCount, snsifUserName=snsifUserName, snsifIcmpBytes=snsifIcmpBytes, snsifOutMaxThroughput=snsifOutMaxThroughput, snsifMask=snsifMask, snsifType=snsifType, snsif=snsif, snsifTable=snsifTable, snsifEntry=snsifEntry, snsifOutIcmpBytes=snsifOutIcmpBytes, snsifPktBlocked=snsifPktBlocked, snsifOutTcpBytes=snsifOutTcpBytes, snsifTcpConn=snsifTcpConn, snsifTcpConnCount=snsifTcpConnCount, snsifInMaxThroughput=snsifInMaxThroughput, PYSNMP_MODULE_ID=snsif, snsifUdpBytes=snsifUdpBytes, snsifOutCurThroughput=snsifOutCurThroughput, snsifTotalBytes=snsifTotalBytes, snsifPktAccepted=snsifPktAccepted, snsifPktFragmented=snsifPktFragmented, snsifInCurThroughput=snsifInCurThroughput, snsifInIcmpBytes=snsifInIcmpBytes, snsifTcpBytes=snsifTcpBytes, snsifInTotalBytes=snsifInTotalBytes, snsifProtected=snsifProtected, snsifCurThroughput=snsifCurThroughput, snsifInUdpBytes=snsifInUdpBytes, snsifName=snsifName, snsifDrvName=snsifDrvName)
