#
# PySNMP MIB module IPVS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/kemp/IPVS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:33:09 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
one4net, = mibBuilder.importSymbols("ONE4NET-MIB", "one4net")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, Opaque, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, IpAddress, Unsigned32, ObjectIdentity, Gauge32, Counter32, ModuleIdentity, MibIdentifier, Integer32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Opaque", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "IpAddress", "Unsigned32", "ObjectIdentity", "Gauge32", "Counter32", "ModuleIdentity", "MibIdentifier", "Integer32", "Bits", "NotificationType")
DisplayString, TruthValue, TextualConvention, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "TimeInterval")
ipvs = ModuleIdentity((1, 3, 6, 1, 4, 1, 12196, 12))
ipvs.setRevisions(('2011-12-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipvs.setRevisionsDescriptions(('version 6.0',))
if mibBuilder.loadTexts: ipvs.setLastUpdated('201112010000Z')
if mibBuilder.loadTexts: ipvs.setOrganization('KEMP Technologies')
if mibBuilder.loadTexts: ipvs.setContactInfo('email:      support@kemptechnologies.com')
if mibBuilder.loadTexts: ipvs.setDescription('Load Master metrics.')
ipvsVSTable = MibTable((1, 3, 6, 1, 4, 1, 12196, 12, 1), )
if mibBuilder.loadTexts: ipvsVSTable.setStatus('current')
if mibBuilder.loadTexts: ipvsVSTable.setDescription('A table containing ipvs Virtual Service (VS) specific information.')
ipvsRSTable = MibTable((1, 3, 6, 1, 4, 1, 12196, 12, 2), )
if mibBuilder.loadTexts: ipvsRSTable.setStatus('current')
if mibBuilder.loadTexts: ipvsRSTable.setDescription('A table containing ipvs Real Server (RS) specific information.')
ipvsRSTotalTable = MibTable((1, 3, 6, 1, 4, 1, 12196, 12, 8), )
if mibBuilder.loadTexts: ipvsRSTotalTable.setStatus('current')
if mibBuilder.loadTexts: ipvsRSTotalTable.setDescription('A table containing Totals for Real Server (RS) specific information.')
rsTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12196, 12, 8, 1), ).setIndexNames((0, "IPVS-MIB", "totRSidx"))
if mibBuilder.loadTexts: rsTotalEntry.setStatus('current')
if mibBuilder.loadTexts: rsTotalEntry.setDescription('Totals for an RS')
totRSidx = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: totRSidx.setStatus('current')
if mibBuilder.loadTexts: totRSidx.setDescription('RS Index ')
totRSDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024)))
if mibBuilder.loadTexts: totRSDesc.setStatus('current')
if mibBuilder.loadTexts: totRSDesc.setDescription('RS description')
totRSConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totRSConns.setStatus('current')
if mibBuilder.loadTexts: totRSConns.setDescription('the total number of connections for this RS')
totRSInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totRSInPkts.setStatus('current')
if mibBuilder.loadTexts: totRSInPkts.setDescription('the total number of incoming pakets to this RS')
totRSOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totRSOutPkts.setStatus('current')
if mibBuilder.loadTexts: totRSOutPkts.setDescription('the total number of outgoing pakets from this RS')
totRSInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totRSInBytes.setStatus('current')
if mibBuilder.loadTexts: totRSInBytes.setDescription('the total number of incoming bytes from this RS')
totRSOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totRSOutBytes.setStatus('current')
if mibBuilder.loadTexts: totRSOutBytes.setDescription('the total number of outgoing bytes from this RS')
totRSActiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totRSActiveConns.setStatus('current')
if mibBuilder.loadTexts: totRSActiveConns.setDescription('the number of active connection for this RS')
totRSInactiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totRSInactiveConns.setStatus('current')
if mibBuilder.loadTexts: totRSInactiveConns.setDescription('the number of inactive connection for this RS')
vsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12196, 12, 1, 1), ).setIndexNames((0, "IPVS-MIB", "vSidx"))
if mibBuilder.loadTexts: vsEntry.setStatus('current')
if mibBuilder.loadTexts: vsEntry.setDescription('information about a VS')
vSidx = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSidx.setStatus('current')
if mibBuilder.loadTexts: vSidx.setDescription('Unique VS Id')
vSDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSDesc.setStatus('current')
if mibBuilder.loadTexts: vSDesc.setDescription('VS description')
vSConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSConns.setStatus('current')
if mibBuilder.loadTexts: vSConns.setDescription('the total number of connections for this VS')
vSInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSInPkts.setStatus('current')
if mibBuilder.loadTexts: vSInPkts.setDescription('the total number of incomming pakets to this VS')
vSOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSOutPkts.setStatus('current')
if mibBuilder.loadTexts: vSOutPkts.setDescription('the total number of outgoing pakets from this VS')
vSInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSInBytes.setStatus('current')
if mibBuilder.loadTexts: vSInBytes.setDescription('the total number of incomming bytes to this VS')
vSOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSOutBytes.setStatus('current')
if mibBuilder.loadTexts: vSOutBytes.setDescription('the number of outgoing bytes from this VS')
vSActivConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSActivConns.setStatus('current')
if mibBuilder.loadTexts: vSActivConns.setDescription('the current number of connections for this VS')
rsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1), ).setIndexNames((0, "IPVS-MIB", "rSidx"))
if mibBuilder.loadTexts: rsEntry.setStatus('current')
if mibBuilder.loadTexts: rsEntry.setDescription('information about a RS')
rSidx = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024)))
if mibBuilder.loadTexts: rSidx.setStatus('current')
if mibBuilder.loadTexts: rSidx.setDescription('Unique Id of RS')
rSVSidx = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSVSidx.setStatus('current')
if mibBuilder.loadTexts: rSVSidx.setDescription('Id of associated VS')
rSDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSDesc.setStatus('current')
if mibBuilder.loadTexts: rSDesc.setDescription('RS description')
rSConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSConns.setStatus('current')
if mibBuilder.loadTexts: rSConns.setDescription('the total number of connections for this RS')
rSInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSInPkts.setStatus('current')
if mibBuilder.loadTexts: rSInPkts.setDescription('the total number of incoming pakets to this RS')
rSOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSOutPkts.setStatus('current')
if mibBuilder.loadTexts: rSOutPkts.setDescription('the total number of outgoing pakets from this RS')
rSInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSInBytes.setStatus('current')
if mibBuilder.loadTexts: rSInBytes.setDescription('the total number of incoming bytes from this RS')
rSOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSOutBytes.setStatus('current')
if mibBuilder.loadTexts: rSOutBytes.setDescription('the total number of outgoing bytes from this RS')
rSActiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSActiveConns.setStatus('current')
if mibBuilder.loadTexts: rSActiveConns.setDescription('the number of active connection for this RS')
rSInactiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSInactiveConns.setStatus('current')
if mibBuilder.loadTexts: rSInactiveConns.setDescription('the number of inactive connection for this RS')
rSWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSWeight.setStatus('current')
if mibBuilder.loadTexts: rSWeight.setDescription('the current weight of this RS')
conns = MibScalar((1, 3, 6, 1, 4, 1, 12196, 12, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: conns.setStatus('current')
if mibBuilder.loadTexts: conns.setDescription('Total number of connections handled for all VS')
inPkts = MibScalar((1, 3, 6, 1, 4, 1, 12196, 12, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inPkts.setStatus('current')
if mibBuilder.loadTexts: inPkts.setDescription('Total number of incoming packets for all VS')
outPkts = MibScalar((1, 3, 6, 1, 4, 1, 12196, 12, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outPkts.setStatus('current')
if mibBuilder.loadTexts: outPkts.setDescription('Total number of outgoing packets for all VS')
inBytes = MibScalar((1, 3, 6, 1, 4, 1, 12196, 12, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inBytes.setStatus('current')
if mibBuilder.loadTexts: inBytes.setDescription('Total number of incoming bytes for all VS')
outBytes = MibScalar((1, 3, 6, 1, 4, 1, 12196, 12, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outBytes.setStatus('current')
if mibBuilder.loadTexts: outBytes.setDescription('Total number of outgoing bytes for all VS')
mibBuilder.exportSymbols("IPVS-MIB", rSWeight=rSWeight, ipvsRSTotalTable=ipvsRSTotalTable, totRSActiveConns=totRSActiveConns, vSInBytes=vSInBytes, outPkts=outPkts, totRSConns=totRSConns, inPkts=inPkts, totRSidx=totRSidx, vSActivConns=vSActivConns, conns=conns, vSOutBytes=vSOutBytes, rSOutPkts=rSOutPkts, ipvsRSTable=ipvsRSTable, vSDesc=vSDesc, rSVSidx=rSVSidx, totRSInactiveConns=totRSInactiveConns, outBytes=outBytes, vSidx=vSidx, totRSInBytes=totRSInBytes, vsEntry=vsEntry, ipvsVSTable=ipvsVSTable, totRSOutBytes=totRSOutBytes, vSConns=vSConns, rSConns=rSConns, totRSOutPkts=totRSOutPkts, totRSDesc=totRSDesc, vSInPkts=vSInPkts, rSInPkts=rSInPkts, rSActiveConns=rSActiveConns, rSOutBytes=rSOutBytes, inBytes=inBytes, rSInactiveConns=rSInactiveConns, rsEntry=rsEntry, vSOutPkts=vSOutPkts, ipvs=ipvs, PYSNMP_MODULE_ID=ipvs, rSInBytes=rSInBytes, totRSInPkts=totRSInPkts, rSidx=rSidx, rsTotalEntry=rsTotalEntry, rSDesc=rSDesc)
