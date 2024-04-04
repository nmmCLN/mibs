#
# PySNMP MIB module TELDAT-MON-CommonInfo-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-MON-CommonInfo-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:39 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, NotificationType, Gauge32, ObjectIdentity, Unsigned32, ModuleIdentity, Integer32, Counter64, IpAddress, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Integer32", "Counter64", "IpAddress", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
telProdNpMonitSistema, telProdNpMonInterfRouter, telProdNpMonInterface = mibBuilder.importSymbols("TELDAT-SW-STRUCTURE-MIB", "telProdNpMonitSistema", "telProdNpMonInterfRouter", "telProdNpMonInterface")
telProdNpMonSistemMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1))
telProdNpMonSistemMemSize = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemSize.setStatus('obsolete')
telProdNpMonSistemMemAvailable = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemAvailable.setStatus('obsolete')
telProdNpMonSistemMemPooldissize = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPooldissize.setStatus('obsolete')
telProdNpMonSistemMemPooldisavailable = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPooldisavailable.setStatus('obsolete')
telProdNpMonSistemMemPoolmdissize = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPoolmdissize.setStatus('obsolete')
telProdNpMonSistemMemPoolmdisavailable = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPoolmdisavailable.setStatus('obsolete')
telProdNpMonSistemMemPooltsize = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPooltsize.setStatus('obsolete')
telProdNpMonSistemMemPooltavailable = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPooltavailable.setStatus('obsolete')
telProdNpMonSistemMemPoolpsize = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPoolpsize.setStatus('obsolete')
telProdNpMonSistemMemPoolpavailable = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPoolpavailable.setStatus('obsolete')
telProdNpMonSistemMemPool0size = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPool0size.setStatus('obsolete')
telProdNpMonSistemMemPool0restpart = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPool0restpart.setStatus('obsolete')
telProdNpMonSistemMemPool0available = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPool0available.setStatus('obsolete')
telProdNpMonSistemMemPool1size = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPool1size.setStatus('mandatory')
telProdNpMonSistemMemPool1restpart = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPool1restpart.setStatus('mandatory')
telProdNpMonSistemMemPool1available = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPool1available.setStatus('mandatory')
telProdNpMonSistemMemPool2size = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPool2size.setStatus('obsolete')
telProdNpMonSistemMemPool2restpart = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPool2restpart.setStatus('obsolete')
telProdNpMonSistemMemPool2available = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPool2available.setStatus('obsolete')
telProdNpMonSistemMemPoolisize = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPoolisize.setStatus('obsolete')
telProdNpMonSistemMemPoolirestpart = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPoolirestpart.setStatus('obsolete')
telProdNpMonSistemMemPooliavailable = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPooliavailable.setStatus('obsolete')
telProdNpMonSistemMemPooldlssize = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPooldlssize.setStatus('obsolete')
telProdNpMonSistemMemPooldlsrestpart = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPooldlsrestpart.setStatus('obsolete')
telProdNpMonSistemMemPooldlsavailable = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemPooldlsavailable.setStatus('obsolete')
telProdNpMonSistemMemTotal = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemTotal.setStatus('mandatory')
telProdNpMonSistemMemTotalcache = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemTotalcache.setStatus('mandatory')
telProdNpMonSistemMemFreecache = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemFreecache.setStatus('mandatory')
telProdNpMonSistemMemTotalnoncache = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemTotalnoncache.setStatus('mandatory')
telProdNpMonSistemMemFreenoncache = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemFreenoncache.setStatus('mandatory')
telProdNpMonSistemMemCaches = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(30, 30)).setFixedLength(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemCaches.setStatus('mandatory')
telProdNpMonSistemMemFlash = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemFlash.setStatus('mandatory')
telProdNpMonSistemMemFreeglobbuffer = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemFreeglobbuffer.setStatus('mandatory')
telProdNpMonSistemMemHeap = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemHeap.setStatus('obsolete')
telProdNpMonSistemMemIcused = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemIcused.setStatus('obsolete')
telProdNpMonSistemMemIcindex = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemIcindex.setStatus('obsolete')
telProdNpMonSistemMemTc = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemMemTc.setStatus('obsolete')
telProdNpMonSistemFan = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 3))
telProdNpMonSistemFanCpu = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemFanCpu.setStatus('mandatory')
telProdNpMonSistemFanCpuPerCent = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemFanCpuPerCent.setStatus('mandatory')
telProdNpMonSistemFanCase = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemFanCase.setStatus('mandatory')
telProdNpMonSistemFanCasePerCent = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonSistemFanCasePerCent.setStatus('mandatory')
telProdNpMonPoeCardsTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 4), )
if mibBuilder.loadTexts: telProdNpMonPoeCardsTable.setStatus('mandatory')
telProdNpMonPoeCardsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 4, 1), ).setIndexNames((0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonPoeCardsInd"))
if mibBuilder.loadTexts: telProdNpMonPoeCardsEntry.setStatus('mandatory')
telProdNpMonPoeCardsInd = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonPoeCardsInd.setStatus('mandatory')
telProdNpMonPoeCardsState = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonPoeCardsState.setStatus('mandatory')
telProdNpMonInterfCommandsTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 1), )
if mibBuilder.loadTexts: telProdNpMonInterfCommandsTable.setStatus('mandatory')
telProdNpMonInterfCommandsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 1, 1), ).setIndexNames((0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfCommandsIfc"))
if mibBuilder.loadTexts: telProdNpMonInterfCommandsEntry.setStatus('mandatory')
telProdNpMonInterfCommandsIfc = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfCommandsIfc.setStatus('mandatory')
telProdNpMonInterfCommandsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("delete", 1), ("valid", 2), ("error", 3), ("undefined", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telProdNpMonInterfCommandsClear.setStatus('mandatory')
telProdNpMonInterfBufferTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1), )
if mibBuilder.loadTexts: telProdNpMonInterfBufferTable.setStatus('mandatory')
telProdNpMonInterfBufferEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1), ).setIndexNames((0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfBufferIfc"))
if mibBuilder.loadTexts: telProdNpMonInterfBufferEntry.setStatus('mandatory')
telProdNpMonInterfBufferIfc = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferIfc.setStatus('obsolete')
telProdNpMonInterfBufferKind = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67))).clone(namedValues=NamedValues(("vi", 1), ("pn", 2), ("pri", 3), ("xeth", 4), ("arpa", 5), ("chp", 6), ("osl", 7), ("eth", 8), ("sl", 9), ("x28", 10), ("dmr", 11), ("tkr", 12), ("snk", 13), ("x25", 14), ("man", 15), ("atr", 16), ("fddi", 17), ("srly", 18), ("ippn", 19), ("fr", 20), ("ppp", 21), ("bdg", 22), ("null", 23), ("isdnb", 24), ("sdlc", 25), ("v25b", 26), ("routernode", 27), ("noderouter", 28), ("isdnd", 29), ("xot", 30), ("int270", 31), ("tnip", 32), ("mppp", 33), ("atm", 34), ("subatm", 35), ("ipsec", 36), ("bri", 37), ("x25fak", 38), ("isdnbfak", 39), ("isdndfak", 40), ("xotfak", 41), ("int270fak", 42), ("asdp", 43), ("syncsl", 44), ("asyncsl", 45), ("aptb", 46), ("dialrout", 47), ("arly", 48), ("mem", 49), ("vlaneth", 50), ("voip", 51), ("l2tp", 52), ("bvi", 53), ("scada", 54), ("wlan", 55), ("sepi", 56), ("eibz", 57), ("gpio", 58), ("autosl", 59), ("mdmemu", 60), ("frsub", 61), ("bvisub", 62), ("nic", 63), ("dip", 64), ("iec101gw", 65), ("gps", 66), ("gpsdatasl", 67)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferKind.setStatus('mandatory')
telProdNpMonInterfBufferOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferOrder.setStatus('mandatory')
telProdNpMonInterfBufferReq = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferReq.setStatus('mandatory')
telProdNpMonInterfBufferAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferAlloc.setStatus('mandatory')
telProdNpMonInterfBufferLow = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferLow.setStatus('mandatory')
telProdNpMonInterfBufferCurr = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferCurr.setStatus('mandatory')
telProdNpMonInterfBufferHdr = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferHdr.setStatus('mandatory')
telProdNpMonInterfBufferWrap = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferWrap.setStatus('mandatory')
telProdNpMonInterfBufferData = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferData.setStatus('mandatory')
telProdNpMonInterfBufferTrail = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferTrail.setStatus('mandatory')
telProdNpMonInterfBufferTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferTotal.setStatus('mandatory')
telProdNpMonInterfBufferAlloc2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfBufferAlloc2.setStatus('mandatory')
telProdNpMonInterfGeneralTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2), )
if mibBuilder.loadTexts: telProdNpMonInterfGeneralTable.setStatus('mandatory')
telProdNpMonInterfGeneralEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1), ).setIndexNames((0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfGeneralIfc"))
if mibBuilder.loadTexts: telProdNpMonInterfGeneralEntry.setStatus('mandatory')
telProdNpMonInterfGeneralIfc = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfGeneralIfc.setStatus('obsolete')
telProdNpMonInterfGeneralKind = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67))).clone(namedValues=NamedValues(("vi", 1), ("pn", 2), ("pri", 3), ("xeth", 4), ("arpa", 5), ("chp", 6), ("osl", 7), ("eth", 8), ("sl", 9), ("x28", 10), ("dmr", 11), ("tkr", 12), ("snk", 13), ("x25", 14), ("man", 15), ("atr", 16), ("fddi", 17), ("srly", 18), ("ippn", 19), ("fr", 20), ("ppp", 21), ("bdg", 22), ("null", 23), ("isdnb", 24), ("sdlc", 25), ("v25b", 26), ("routernode", 27), ("noderouter", 28), ("isdnd", 29), ("xot", 30), ("int270", 31), ("tnip", 32), ("mppp", 33), ("atm", 34), ("subatm", 35), ("ipsec", 36), ("bri", 37), ("x25fak", 38), ("isdnbfak", 39), ("isdndfak", 40), ("xotfak", 41), ("int270fak", 42), ("asdp", 43), ("syncsl", 44), ("asyncsl", 45), ("aptb", 46), ("dialrout", 47), ("arly", 48), ("mem", 49), ("vlaneth", 50), ("voip", 51), ("l2tp", 52), ("bvi", 53), ("scada", 54), ("wlan", 55), ("sepi", 56), ("eibz", 57), ("gpio", 58), ("autosl", 59), ("mdmemu", 60), ("frsub", 61), ("bvisub", 62), ("nic", 63), ("dip", 64), ("iec101gw", 65), ("gps", 66), ("gpsdatasl", 67)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfGeneralKind.setStatus('mandatory')
telProdNpMonInterfGeneralOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfGeneralOrder.setStatus('mandatory')
telProdNpMonInterfGeneralCsr = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfGeneralCsr.setStatus('mandatory')
telProdNpMonInterfGeneralVect = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfGeneralVect.setStatus('mandatory')
telProdNpMonInterfGeneralTestvalid = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfGeneralTestvalid.setStatus('mandatory')
telProdNpMonInterfGeneralTestfailure = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfGeneralTestfailure.setStatus('mandatory')
telProdNpMonInterfGeneralMaintenFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfGeneralMaintenFailure.setStatus('mandatory')
telProdNpMonInterfErrorsTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3), )
if mibBuilder.loadTexts: telProdNpMonInterfErrorsTable.setStatus('mandatory')
telProdNpMonInterfErrorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1), ).setIndexNames((0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfErrorsIfc"))
if mibBuilder.loadTexts: telProdNpMonInterfErrorsEntry.setStatus('mandatory')
telProdNpMonInterfErrorsIfc = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfErrorsIfc.setStatus('obsolete')
telProdNpMonInterfErrorsKind = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67))).clone(namedValues=NamedValues(("vi", 1), ("pn", 2), ("pri", 3), ("xeth", 4), ("arpa", 5), ("chp", 6), ("osl", 7), ("eth", 8), ("sl", 9), ("x28", 10), ("dmr", 11), ("tkr", 12), ("snk", 13), ("x25", 14), ("man", 15), ("atr", 16), ("fddi", 17), ("srly", 18), ("ippn", 19), ("fr", 20), ("ppp", 21), ("bdg", 22), ("null", 23), ("isdnb", 24), ("sdlc", 25), ("v25b", 26), ("routernode", 27), ("noderouter", 28), ("isdnd", 29), ("xot", 30), ("int270", 31), ("tnip", 32), ("mppp", 33), ("atm", 34), ("subatm", 35), ("ipsec", 36), ("bri", 37), ("x25fak", 38), ("isdnbfak", 39), ("isdndfak", 40), ("xotfak", 41), ("int270fak", 42), ("asdp", 43), ("syncsl", 44), ("asyncsl", 45), ("aptb", 46), ("dialrout", 47), ("arly", 48), ("mem", 49), ("vlaneth", 50), ("voip", 51), ("l2tp", 52), ("bvi", 53), ("scada", 54), ("wlan", 55), ("sepi", 56), ("eibz", 57), ("gpio", 58), ("autosl", 59), ("mdmemu", 60), ("frsub", 61), ("bvisub", 62), ("nic", 63), ("dip", 64), ("iec101gw", 65), ("gps", 66), ("gpsdatasl", 67)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfErrorsKind.setStatus('mandatory')
telProdNpMonInterfErrorsOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfErrorsOrder.setStatus('mandatory')
telProdNpMonInterfErrorsIdiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfErrorsIdiscard.setStatus('mandatory')
telProdNpMonInterfErrorsIerrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfErrorsIerrors.setStatus('mandatory')
telProdNpMonInterfErrorsIunkprot = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfErrorsIunkprot.setStatus('mandatory')
telProdNpMonInterfErrorsOflowdrop = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfErrorsOflowdrop.setStatus('mandatory')
telProdNpMonInterfErrorsOdiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfErrorsOdiscard.setStatus('mandatory')
telProdNpMonInterfErrorsOerrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfErrorsOerrors.setStatus('mandatory')
telProdNpMonInterfQueueTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4), )
if mibBuilder.loadTexts: telProdNpMonInterfQueueTable.setStatus('mandatory')
telProdNpMonInterfQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1), ).setIndexNames((0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfQueueIfc"))
if mibBuilder.loadTexts: telProdNpMonInterfQueueEntry.setStatus('mandatory')
telProdNpMonInterfQueueIfc = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfQueueIfc.setStatus('obsolete')
telProdNpMonInterfQueueKind = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67))).clone(namedValues=NamedValues(("vi", 1), ("pn", 2), ("pri", 3), ("xeth", 4), ("arpa", 5), ("chp", 6), ("osl", 7), ("eth", 8), ("sl", 9), ("x28", 10), ("dmr", 11), ("tkr", 12), ("snk", 13), ("x25", 14), ("man", 15), ("atr", 16), ("fddi", 17), ("srly", 18), ("ippn", 19), ("fr", 20), ("ppp", 21), ("bdg", 22), ("null", 23), ("isdnb", 24), ("sdlc", 25), ("v25b", 26), ("routernode", 27), ("noderouter", 28), ("isdnd", 29), ("xot", 30), ("int270", 31), ("tnip", 32), ("mppp", 33), ("atm", 34), ("subatm", 35), ("ipsec", 36), ("bri", 37), ("x25fak", 38), ("isdnbfak", 39), ("isdndfak", 40), ("xotfak", 41), ("int270fak", 42), ("asdp", 43), ("syncsl", 44), ("asyncsl", 45), ("aptb", 46), ("dialrout", 47), ("arly", 48), ("mem", 49), ("vlaneth", 50), ("voip", 51), ("l2tp", 52), ("bvi", 53), ("scada", 54), ("wlan", 55), ("sepi", 56), ("eibz", 57), ("gpio", 58), ("autosl", 59), ("mdmemu", 60), ("frsub", 61), ("bvisub", 62), ("nic", 63), ("dip", 64), ("iec101gw", 65), ("gps", 66), ("gpsdatasl", 67)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfQueueKind.setStatus('mandatory')
telProdNpMonInterfQueueOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfQueueOrder.setStatus('mandatory')
telProdNpMonInterfQueueIalloc = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfQueueIalloc.setStatus('mandatory')
telProdNpMonInterfQueueIlow = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfQueueIlow.setStatus('mandatory')
telProdNpMonInterfQueueIcurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfQueueIcurrent.setStatus('mandatory')
telProdNpMonInterfQueueOfair = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfQueueOfair.setStatus('mandatory')
telProdNpMonInterfQueueOcurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfQueueOcurrent.setStatus('mandatory')
telProdNpMonInterfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5), )
if mibBuilder.loadTexts: telProdNpMonInterfStatsTable.setStatus('mandatory')
telProdNpMonInterfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1), ).setIndexNames((0, "TELDAT-MON-CommonInfo-MIB", "telProdNpMonInterfStatsIfc"))
if mibBuilder.loadTexts: telProdNpMonInterfStatsEntry.setStatus('mandatory')
telProdNpMonInterfStatsIfc = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfStatsIfc.setStatus('obsolete')
telProdNpMonInterfStatsKind = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67))).clone(namedValues=NamedValues(("vi", 1), ("pn", 2), ("pri", 3), ("xeth", 4), ("arpa", 5), ("chp", 6), ("osl", 7), ("eth", 8), ("sl", 9), ("x28", 10), ("dmr", 11), ("tkr", 12), ("snk", 13), ("x25", 14), ("man", 15), ("atr", 16), ("fddi", 17), ("srly", 18), ("ippn", 19), ("fr", 20), ("ppp", 21), ("bdg", 22), ("null", 23), ("isdnb", 24), ("sdlc", 25), ("v25b", 26), ("routernode", 27), ("noderouter", 28), ("isdnd", 29), ("xot", 30), ("int270", 31), ("tnip", 32), ("mppp", 33), ("atm", 34), ("subatm", 35), ("ipsec", 36), ("bri", 37), ("x25fak", 38), ("isdnbfak", 39), ("isdndfak", 40), ("xotfak", 41), ("int270fak", 42), ("asdp", 43), ("syncsl", 44), ("asyncsl", 45), ("aptb", 46), ("dialrout", 47), ("arly", 48), ("mem", 49), ("vlaneth", 50), ("voip", 51), ("l2tp", 52), ("bvi", 53), ("scada", 54), ("wlan", 55), ("sepi", 56), ("eibz", 57), ("gpio", 58), ("autosl", 59), ("mdmemu", 60), ("frsub", 61), ("bvisub", 62), ("nic", 63), ("dip", 64), ("iec101gw", 65), ("gps", 66), ("gpsdatasl", 67)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfStatsKind.setStatus('mandatory')
telProdNpMonInterfStatsOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfStatsOrder.setStatus('mandatory')
telProdNpMonInterfStatsUnipkrcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfStatsUnipkrcv.setStatus('mandatory')
telProdNpMonInterfStatsMulpkrcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfStatsMulpkrcv.setStatus('mandatory')
telProdNpMonInterfStatsBytesrcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfStatsBytesrcv.setStatus('mandatory')
telProdNpMonInterfStatsPkxt = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfStatsPkxt.setStatus('mandatory')
telProdNpMonInterfStatsBytesxt = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telProdNpMonInterfStatsBytesxt.setStatus('mandatory')
mibBuilder.exportSymbols("TELDAT-MON-CommonInfo-MIB", telProdNpMonInterfBufferAlloc2=telProdNpMonInterfBufferAlloc2, telProdNpMonSistemMemPooldlssize=telProdNpMonSistemMemPooldlssize, telProdNpMonSistemFanCpu=telProdNpMonSistemFanCpu, telProdNpMonInterfBufferIfc=telProdNpMonInterfBufferIfc, telProdNpMonInterfGeneralCsr=telProdNpMonInterfGeneralCsr, telProdNpMonInterfBufferReq=telProdNpMonInterfBufferReq, telProdNpMonInterfGeneralKind=telProdNpMonInterfGeneralKind, telProdNpMonInterfStatsIfc=telProdNpMonInterfStatsIfc, telProdNpMonInterfBufferData=telProdNpMonInterfBufferData, telProdNpMonInterfQueueOrder=telProdNpMonInterfQueueOrder, telProdNpMonInterfErrorsEntry=telProdNpMonInterfErrorsEntry, telProdNpMonSistemMemPool0size=telProdNpMonSistemMemPool0size, telProdNpMonInterfBufferKind=telProdNpMonInterfBufferKind, telProdNpMonInterfBufferLow=telProdNpMonInterfBufferLow, telProdNpMonSistemMemPool0restpart=telProdNpMonSistemMemPool0restpart, telProdNpMonInterfErrorsIfc=telProdNpMonInterfErrorsIfc, telProdNpMonInterfBufferAlloc=telProdNpMonInterfBufferAlloc, telProdNpMonInterfStatsPkxt=telProdNpMonInterfStatsPkxt, telProdNpMonSistemMemPoolisize=telProdNpMonSistemMemPoolisize, telProdNpMonInterfErrorsTable=telProdNpMonInterfErrorsTable, telProdNpMonInterfQueueKind=telProdNpMonInterfQueueKind, telProdNpMonSistemMemPoolmdisavailable=telProdNpMonSistemMemPoolmdisavailable, telProdNpMonInterfCommandsIfc=telProdNpMonInterfCommandsIfc, telProdNpMonInterfCommandsClear=telProdNpMonInterfCommandsClear, telProdNpMonInterfStatsBytesxt=telProdNpMonInterfStatsBytesxt, telProdNpMonInterfGeneralVect=telProdNpMonInterfGeneralVect, telProdNpMonInterfCommandsTable=telProdNpMonInterfCommandsTable, telProdNpMonSistemMemAvailable=telProdNpMonSistemMemAvailable, telProdNpMonInterfCommandsEntry=telProdNpMonInterfCommandsEntry, telProdNpMonSistemMemTotalnoncache=telProdNpMonSistemMemTotalnoncache, telProdNpMonInterfGeneralTable=telProdNpMonInterfGeneralTable, telProdNpMonPoeCardsEntry=telProdNpMonPoeCardsEntry, telProdNpMonSistemMemPoolirestpart=telProdNpMonSistemMemPoolirestpart, telProdNpMonInterfQueueIlow=telProdNpMonInterfQueueIlow, telProdNpMonSistemFan=telProdNpMonSistemFan, telProdNpMonInterfErrorsOflowdrop=telProdNpMonInterfErrorsOflowdrop, telProdNpMonSistemMemPooltavailable=telProdNpMonSistemMemPooltavailable, telProdNpMonInterfGeneralIfc=telProdNpMonInterfGeneralIfc, telProdNpMonInterfStatsTable=telProdNpMonInterfStatsTable, telProdNpMonInterfQueueIalloc=telProdNpMonInterfQueueIalloc, telProdNpMonInterfStatsUnipkrcv=telProdNpMonInterfStatsUnipkrcv, telProdNpMonInterfStatsMulpkrcv=telProdNpMonInterfStatsMulpkrcv, telProdNpMonInterfQueueEntry=telProdNpMonInterfQueueEntry, telProdNpMonInterfStatsKind=telProdNpMonInterfStatsKind, telProdNpMonInterfErrorsOrder=telProdNpMonInterfErrorsOrder, telProdNpMonSistemMemTotal=telProdNpMonSistemMemTotal, telProdNpMonSistemMemPool1size=telProdNpMonSistemMemPool1size, telProdNpMonSistemMemCaches=telProdNpMonSistemMemCaches, telProdNpMonSistemMemPool0available=telProdNpMonSistemMemPool0available, telProdNpMonPoeCardsState=telProdNpMonPoeCardsState, telProdNpMonInterfErrorsIerrors=telProdNpMonInterfErrorsIerrors, telProdNpMonSistemMemFreenoncache=telProdNpMonSistemMemFreenoncache, telProdNpMonInterfBufferTable=telProdNpMonInterfBufferTable, telProdNpMonSistemMemPooltsize=telProdNpMonSistemMemPooltsize, telProdNpMonSistemMemIcindex=telProdNpMonSistemMemIcindex, telProdNpMonSistemMemPooldlsrestpart=telProdNpMonSistemMemPooldlsrestpart, telProdNpMonSistemMemPooliavailable=telProdNpMonSistemMemPooliavailable, telProdNpMonInterfBufferWrap=telProdNpMonInterfBufferWrap, telProdNpMonInterfQueueTable=telProdNpMonInterfQueueTable, telProdNpMonSistemFanCase=telProdNpMonSistemFanCase, telProdNpMonInterfQueueIfc=telProdNpMonInterfQueueIfc, telProdNpMonSistemMemSize=telProdNpMonSistemMemSize, telProdNpMonSistemMemPool2size=telProdNpMonSistemMemPool2size, telProdNpMonInterfQueueOfair=telProdNpMonInterfQueueOfair, telProdNpMonInterfErrorsOerrors=telProdNpMonInterfErrorsOerrors, telProdNpMonInterfErrorsIdiscard=telProdNpMonInterfErrorsIdiscard, telProdNpMonInterfBufferHdr=telProdNpMonInterfBufferHdr, telProdNpMonSistemFanCpuPerCent=telProdNpMonSistemFanCpuPerCent, telProdNpMonInterfStatsOrder=telProdNpMonInterfStatsOrder, telProdNpMonSistemMemPool2available=telProdNpMonSistemMemPool2available, telProdNpMonSistemMemPool1restpart=telProdNpMonSistemMemPool1restpart, telProdNpMonSistemMemory=telProdNpMonSistemMemory, telProdNpMonInterfBufferTotal=telProdNpMonInterfBufferTotal, telProdNpMonSistemMemFreecache=telProdNpMonSistemMemFreecache, telProdNpMonPoeCardsTable=telProdNpMonPoeCardsTable, telProdNpMonInterfGeneralTestfailure=telProdNpMonInterfGeneralTestfailure, telProdNpMonInterfBufferEntry=telProdNpMonInterfBufferEntry, telProdNpMonSistemMemPoolpsize=telProdNpMonSistemMemPoolpsize, telProdNpMonSistemFanCasePerCent=telProdNpMonSistemFanCasePerCent, telProdNpMonInterfErrorsKind=telProdNpMonInterfErrorsKind, telProdNpMonInterfQueueIcurrent=telProdNpMonInterfQueueIcurrent, telProdNpMonSistemMemPooldisavailable=telProdNpMonSistemMemPooldisavailable, telProdNpMonSistemMemPoolmdissize=telProdNpMonSistemMemPoolmdissize, telProdNpMonSistemMemFlash=telProdNpMonSistemMemFlash, telProdNpMonInterfGeneralMaintenFailure=telProdNpMonInterfGeneralMaintenFailure, telProdNpMonInterfGeneralTestvalid=telProdNpMonInterfGeneralTestvalid, telProdNpMonInterfBufferTrail=telProdNpMonInterfBufferTrail, telProdNpMonInterfBufferOrder=telProdNpMonInterfBufferOrder, telProdNpMonSistemMemTc=telProdNpMonSistemMemTc, telProdNpMonSistemMemPool1available=telProdNpMonSistemMemPool1available, telProdNpMonPoeCardsInd=telProdNpMonPoeCardsInd, telProdNpMonInterfBufferCurr=telProdNpMonInterfBufferCurr, telProdNpMonInterfStatsEntry=telProdNpMonInterfStatsEntry, telProdNpMonSistemMemTotalcache=telProdNpMonSistemMemTotalcache, telProdNpMonSistemMemHeap=telProdNpMonSistemMemHeap, telProdNpMonInterfStatsBytesrcv=telProdNpMonInterfStatsBytesrcv, telProdNpMonSistemMemFreeglobbuffer=telProdNpMonSistemMemFreeglobbuffer, telProdNpMonInterfErrorsIunkprot=telProdNpMonInterfErrorsIunkprot, telProdNpMonSistemMemPoolpavailable=telProdNpMonSistemMemPoolpavailable, telProdNpMonSistemMemPooldlsavailable=telProdNpMonSistemMemPooldlsavailable, telProdNpMonInterfGeneralOrder=telProdNpMonInterfGeneralOrder, telProdNpMonSistemMemPooldissize=telProdNpMonSistemMemPooldissize, telProdNpMonInterfErrorsOdiscard=telProdNpMonInterfErrorsOdiscard, telProdNpMonInterfQueueOcurrent=telProdNpMonInterfQueueOcurrent, telProdNpMonSistemMemIcused=telProdNpMonSistemMemIcused, telProdNpMonSistemMemPool2restpart=telProdNpMonSistemMemPool2restpart, telProdNpMonInterfGeneralEntry=telProdNpMonInterfGeneralEntry)
