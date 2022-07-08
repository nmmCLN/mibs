#
# PySNMP MIB module SL-XPDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-XPDR-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:56 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfTotalCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfTotalCount", "PerfIntervalCount")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Counter64, Counter32, iso, Unsigned32, TimeTicks, Integer32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Counter64", "Counter32", "iso", "Unsigned32", "TimeTicks", "Integer32", "ModuleIdentity", "IpAddress")
DisplayString, RowStatus, TimeStamp, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TimeStamp", "TruthValue", "TextualConvention")
slXpdr = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 8))
if mibBuilder.loadTexts: slXpdr.setLastUpdated('200501250000Z')
if mibBuilder.loadTexts: slXpdr.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slXpdr.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slXpdr.setDescription('This MIB module describes the optical connections.')
slXpdrConn = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1))
slXpdrLastChange = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 8, 6))
slXpdrTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 8, 7))
slXpdrTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 0))
class TsMaskBits(TextualConvention, OctetString):
    description = '100G Tributary Slots Mask Bits 1..80.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 10)

class XpdrServiceType(TextualConvention, Integer32):
    description = 'The service type of the tarsponder.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 87, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 118, 120, 121, 170, 171, 1701))
    namedValues = NamedValues(("ds3Sts1", 1), ("fe", 2), ("escon", 3), ("dvbVideo", 4), ("fc1gFicon", 5), ("gbE", 6), ("fc2g", 7), ("oc3Stm1", 8), ("oc12Stm4", 9), ("oc48Stm16", 10), ("other", 11), ("fc4g", 12), ("infiniband25G", 13), ("otn27g", 14), ("oc24gpon", 15), ("smpteSdi", 16), ("copperFe", 17), ("copperGbe", 18), ("mux2GbE", 19), ("mux4GbE", 20), ("xpdr5G", 21), ("ficon1g", 22), ("ficon2g", 23), ("stm1", 24), ("stm4", 25), ("stm16", 26), ("gpon248", 27), ("ficon4g", 28), ("eth10m", 29), ("xfp10oc192", 30), ("xfp10stm64", 31), ("xfp10GbEWan", 32), ("xfp10GbELan", 33), ("xfp10otu2", 34), ("xfp10GFC", 35), ("xfp10GbEWanStm64", 36), ("mux1GbE", 37), ("mux1GbERegen", 38), ("mux2GbERegen", 39), ("mux4GbERegen", 40), ("fc8g", 41), ("ficon8g", 42), ("mux10GbE", 43), ("syncEgbE", 44), ("noPm10GbE", 45), ("totu2", 46), ("otu1e", 50), ("otu2e", 51), ("otu1f", 52), ("otu2f", 53), ("oc192ToOtu2", 54), ("stm64ToOtu2", 55), ("gbe10WanToOtu2", 56), ("gbe10LanToOtu2A", 57), ("gbe10LanToOtu1e", 58), ("gbe10LanToOtu2e", 59), ("gbe10LanToOtu2B", 60), ("fc10LanToOtu1f", 61), ("fc10LanToOtu2f", 62), ("fc8LanToOtu2", 63), ("otu3", 64), ("oc768", 65), ("stm256", 66), ("otu4", 67), ("gbe40lan", 68), ("gbe100lan", 69), ("fc16g", 70), ("smpteHdSdi", 71), ("smpteSdSdi", 72), ("smpte3gSdi", 73), ("smpte3dSdi", 74), ("smpteHdSdiNtsc", 75), ("smpte3gSdiNtsc", 76), ("fc16gNoIsl", 77), ("fc32g", 78), ("cpri1", 81), ("cpri2", 82), ("cpri3", 83), ("cpri4", 84), ("cpri5", 85), ("cpri6", 86), ("cpri7", 87), ("enc10GbELan", 91), ("enc1GbELan", 92), ("encfc1g", 93), ("encfc2g", 94), ("encfc4g", 95), ("encfc8g", 96), ("encfc16g", 97), ("encfc10g", 98), ("enc1GbE10g", 99), ("encGbe40lan", 100), ("encGbe100lan", 101), ("encOtu2", 102), ("encOtu2e", 103), ("encOtu3", 104), ("encOtu4", 105), ("encOc192", 106), ("encStm64", 107), ("encfc32g", 108), ("encfc16gNoIsl", 110), ("encCpri1", 111), ("encCpri2", 112), ("encCpri3", 113), ("encCpri4", 114), ("encCpri5", 115), ("encCpri6", 116), ("encCpri7", 117), ("enc10GbENoPm", 118), ("otuc2", 120), ("encOtuc2", 121), ("copper10m", 170), ("copper10mAn", 171), ("copperFeAn", 1701))

xpdrConnConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1), )
if mibBuilder.loadTexts: xpdrConnConfigTable.setStatus('current')
if mibBuilder.loadTexts: xpdrConnConfigTable.setDescription('The connection table contains for each\n\t\ttransponding connection a single bi-directional entry.\n\t\tThe index to the table is the ifIndex of both XPDR interfaces.\n\t\tThe ifType valued used for the index is: 196.')
xpdrConnConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1), ).setIndexNames((0, "SL-XPDR-MIB", "xpdrConnConfigIf1"), (0, "SL-XPDR-MIB", "xpdrConnConfigIf2"))
if mibBuilder.loadTexts: xpdrConnConfigEntry.setStatus('current')
if mibBuilder.loadTexts: xpdrConnConfigEntry.setDescription('An entry in the transponding connection table.')
xpdrConnConfigIf1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xpdrConnConfigIf1.setStatus('current')
if mibBuilder.loadTexts: xpdrConnConfigIf1.setDescription('The first XPDR interface.')
xpdrConnConfigIf2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xpdrConnConfigIf2.setStatus('current')
if mibBuilder.loadTexts: xpdrConnConfigIf2.setDescription('The second XPDR interface.')
xpdrConnConfigRateControlAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnConfigRateControlAdmin.setStatus('current')
if mibBuilder.loadTexts: xpdrConnConfigRateControlAdmin.setDescription('This variable ask the rate of the traffic used\n\t\tby this interface. Frequency is in Kbp/s. \t\t\n\t\tThe value 0-30 is used for rate control Bypass.')
xpdrConnConfigRateControlOper = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xpdrConnConfigRateControlOper.setStatus('current')
if mibBuilder.loadTexts: xpdrConnConfigRateControlOper.setDescription('This variable tells the rate of the traffic used\n\t\tby this interface. Frequency is in Kbp/s. \t\t\n\t\tThe value 0 returned for rate control Bypass.')
xpdrConnConfigLosPropagation = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnConfigLosPropagation.setStatus('current')
if mibBuilder.loadTexts: xpdrConnConfigLosPropagation.setDescription('This object is used to detrmine if the LOS propagation should be active.')
xpdrServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 6), XpdrServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrServiceType.setStatus('current')
if mibBuilder.loadTexts: xpdrServiceType.setDescription('The service type of the transponder.')
xpdrConnAddMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnAddMask.setStatus('current')
if mibBuilder.loadTexts: xpdrConnAddMask.setDescription('This object is a bit mask relevant only for 10G Muxponder entry. \n\t\tIt contains a bit for each Muxponder service.\n\t\tTo add a service the management should set the corresponding bit to 1.\n\t\tTo remove a service the bit should be set to 0.\n\t\t\n\t\tFor ODU allocation, the value of xpdrConnAddMask should be set to reflect the odus/time-slots \n\t\tprovisioned for the service according to the following rules:\n\t\ta.\tFor ODU1 the first byte is 0; for ODU0 the first byte is 1.\n\t\tb.\tThe second byte. Is equal to:\n\t\t\ti.\tThe 4 bits of the first nibble correspond to Uplink 1 allocated odus counted from right to left\n\t\t\tii.\tThe 4 bits of the second nibble correspond to Uplink 2 allocated odus counted from right to left \n\t\tc.\tThe Third and Forth bytes keep bit-mask of the allocated time-slots within the odu.')
xpdrMuxInbandAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("standby", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrMuxInbandAdmin.setStatus('current')
if mibBuilder.loadTexts: xpdrMuxInbandAdmin.setDescription('This object is relevant only for muxponder.\n\t\t up value means that the muxponder inband management is enabled.')
xpdrMuxInbandOper = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xpdrMuxInbandOper.setStatus('current')
if mibBuilder.loadTexts: xpdrMuxInbandOper.setDescription('The operational state of the inband interface.')
xpdrDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("bidirectional", 1), ("unidirectionalTx", 2), ("unidirectionalRx", 3), ("loopback", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrDirection.setStatus('current')
if mibBuilder.loadTexts: xpdrDirection.setDescription('This object is used for unidirectional services.\n\t\tThe upper port is the uplink as with the aps configuration.\n\t\tThe transponder on one side should be configured as TX and the peer as RX.')
xpdrConnConfigCpriRateControl = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnConfigCpriRateControl.setStatus('current')
if mibBuilder.loadTexts: xpdrConnConfigCpriRateControl.setDescription('This object is used to detrmine if the CPRI rate control should be active.')
xpdrFaultPropagationDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrFaultPropagationDelay.setStatus('current')
if mibBuilder.loadTexts: xpdrFaultPropagationDelay.setDescription('This object is used to determine the fault propagation delay.\n\t\tThe value 0 mean no delay, the value 1 means 100ms delay, the value 2 means 200ms delay etc.\n\t\t0 is the default value.')
xpdrFecMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrFecMode.setStatus('current')
if mibBuilder.loadTexts: xpdrFecMode.setDescription('This object is used to determine the IEEE FEC mode for 10G and 16G services:\n\t\t0 - No FEC (default)\n\t\t1 - FEC Monitoring\n\t\t2 - FEC Generation\n\t\t3 - FEC Regeneration')
xpdrConnAddMask1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 14), TsMaskBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnAddMask1.setStatus('current')
if mibBuilder.loadTexts: xpdrConnAddMask1.setDescription('This object is a bit mask relevant only for 100G Muxponder entry. \n\t\tIt contains a bit for each tributary slot allocated to the service port from Uplink 1.\n\t\tTo incluse a tributary slot the management should set the corresponding bit to 1.\n\t\tTo remove a tributary slot service the bit should be set to 0.')
xpdrConnAddMask2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 15), TsMaskBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnAddMask2.setStatus('current')
if mibBuilder.loadTexts: xpdrConnAddMask2.setDescription('This object is a bit mask relevant only for 100G Muxponder entry. \n\t\tIt contains a bit for each tributary slot allocated to the service port from Uplink 2.\n\t\tTo incluse a tributary slot the management should set the corresponding bit to 1.\n\t\tTo remove a tributary slot service the bit should be set to 0.\n\t\tThis entry is relevant only for protected services.')
xpdrCryptoUser = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 16), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrCryptoUser.setStatus('current')
if mibBuilder.loadTexts: xpdrCryptoUser.setDescription('The user name of the crypto officer assigned to this service.\n\t\tDefault value is Crypto')
oduXcConnConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2), )
if mibBuilder.loadTexts: oduXcConnConfigTable.setStatus('current')
if mibBuilder.loadTexts: oduXcConnConfigTable.setDescription('Description for 10G:\n\t\t1. The port numbers are:\n\t\t\t0       unassigned \n\t\t\t1..10   ODUs of Uplink 1\n\t\t\t11..20  ODUs of Uplink 2 (not available without 20G or 1+1 license)\n\t\t2. All connections are unidirectional\n\t\t3. P1 is the Source port and P2 is the Sync port\n\t\t4. Port 0 is used as P2 when P1 is dropped\n\t\t5. Port 0 is used as P1 when P2 is added\n\t\t6. In the case of APS the two mate ODUs will apear with oduXcConnConfigProtected=TRUE\n\t\t7. The allocation of ODUs per service port is described in xpdrConnAddMask above\n\t\tDescription for 100G:\n\t\tThe ports are the ifIndex of the tributary slots, where the path byte equals to the tributary slot.')
oduXcConnConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1), ).setIndexNames((0, "SL-XPDR-MIB", "oduXcConnConfigP1"), (0, "SL-XPDR-MIB", "oduXcConnConfigP2"))
if mibBuilder.loadTexts: oduXcConnConfigEntry.setStatus('current')
if mibBuilder.loadTexts: oduXcConnConfigEntry.setDescription('An entry in the ODU connection table. \n\t\t An entry describes uni-directional connection of traffic from P1 (Source port) to port P2 (Sync port).')
oduXcConnConfigP1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oduXcConnConfigP1.setStatus('current')
if mibBuilder.loadTexts: oduXcConnConfigP1.setDescription('The Source port.')
oduXcConnConfigP2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oduXcConnConfigP2.setStatus('current')
if mibBuilder.loadTexts: oduXcConnConfigP2.setDescription('The Sync port.')
oduXcConnConfigProtected = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oduXcConnConfigProtected.setStatus('current')
if mibBuilder.loadTexts: oduXcConnConfigProtected.setDescription('Indication for entry with Protection Mates')
oduXcConnConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oduXcConnConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: oduXcConnConfigRowStatus.setDescription('The Status of this connection entry.')
tribXcConnConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3), )
if mibBuilder.loadTexts: tribXcConnConfigTable.setStatus('current')
if mibBuilder.loadTexts: tribXcConnConfigTable.setDescription('The ports are:\n\t\t\tFor service port - the first tributary (1..80)\n\t\t\tFor Uplink 1 - 100 + first tributary (101..180)\n\t\t\tFor Uplink 2 - 200 + first tributary (201..280)')
tribXcConnConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1), ).setIndexNames((0, "SL-XPDR-MIB", "tribXcConnConfigP1"), (0, "SL-XPDR-MIB", "tribXcConnConfigP2"))
if mibBuilder.loadTexts: tribXcConnConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tribXcConnConfigEntry.setDescription('An entry in the tributary cross connection table. \n\t\t An entry describes uni-directional connection of traffic from P1 (Source port) to port P2 (Sync port).')
tribXcConnConfigP1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tribXcConnConfigP1.setStatus('current')
if mibBuilder.loadTexts: tribXcConnConfigP1.setDescription('The Source port.')
tribXcConnConfigP2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tribXcConnConfigP2.setStatus('current')
if mibBuilder.loadTexts: tribXcConnConfigP2.setDescription('The Sync port.')
tribXcConnServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 3), XpdrServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tribXcConnServiceType.setStatus('current')
if mibBuilder.loadTexts: tribXcConnServiceType.setDescription('The service type of the service.')
tribXcConnMask1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 4), TsMaskBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tribXcConnMask1.setStatus('current')
if mibBuilder.loadTexts: tribXcConnMask1.setDescription('This object is a bit mask relevant only for 100G Muxponder entry. \n\t\tIt contains a bit for each tributary slot allocated to the service port from Uplink 1.\n\t\tTo incluse a tributary slot the management should set the corresponding bit to 1.\n\t\tTo remove a tributary slot service the bit should be set to 0.')
tribXcConnMask2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 5), TsMaskBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tribXcConnMask2.setStatus('current')
if mibBuilder.loadTexts: tribXcConnMask2.setDescription('This object is a bit mask relevant only for 100G Muxponder entry. \n\t\tIt contains a bit for each tributary slot allocated to the service port from Uplink 2.\n\t\tTo incluse a tributary slot the management should set the corresponding bit to 1.\n\t\tTo remove a tributary slot service the bit should be set to 0.\n\t\tThis entry is relevant only for protected services.')
tribXcConnConfigProtected = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tribXcConnConfigProtected.setStatus('current')
if mibBuilder.loadTexts: tribXcConnConfigProtected.setDescription('Indication for entry with Protection Mates')
tribXcConnConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tribXcConnConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: tribXcConnConfigRowStatus.setDescription('The Status of this connection entry.')
smmOwnerMode = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gui", 1), ("ems", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smmOwnerMode.setStatus('current')
if mibBuilder.loadTexts: smmOwnerMode.setDescription('The owner of the SMM tables.')
xpdrConnConfigTableChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 1))
if mibBuilder.loadTexts: xpdrConnConfigTableChange.setStatus('current')
if mibBuilder.loadTexts: xpdrConnConfigTableChange.setDescription('A xpdrConnConfigTableChange trap is sent when the\n\t\tcontent of the xpdrConnConfigTable is changed.')
xpdrConnConfigTableChange0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 0, 1))
if mibBuilder.loadTexts: xpdrConnConfigTableChange0.setStatus('current')
if mibBuilder.loadTexts: xpdrConnConfigTableChange0.setDescription("A xpdrConnConfigTableChange trap is sent when the\n\t\tcontent of the xpdrConnConfigTable is changed.\n\t\tIt is defined to support browsers that don't recognize RFC 2576.")
mibBuilder.exportSymbols("SL-XPDR-MIB", xpdrMuxInbandAdmin=xpdrMuxInbandAdmin, xpdrConnConfigTableChange=xpdrConnConfigTableChange, slXpdrTraps=slXpdrTraps, tribXcConnConfigEntry=tribXcConnConfigEntry, oduXcConnConfigTable=oduXcConnConfigTable, oduXcConnConfigP2=oduXcConnConfigP2, xpdrMuxInbandOper=xpdrMuxInbandOper, slXpdrConn=slXpdrConn, xpdrCryptoUser=xpdrCryptoUser, xpdrFaultPropagationDelay=xpdrFaultPropagationDelay, xpdrConnAddMask=xpdrConnAddMask, xpdrConnConfigEntry=xpdrConnConfigEntry, xpdrConnConfigIf2=xpdrConnConfigIf2, xpdrDirection=xpdrDirection, tribXcConnConfigP2=tribXcConnConfigP2, xpdrConnConfigLosPropagation=xpdrConnConfigLosPropagation, xpdrConnAddMask2=xpdrConnAddMask2, oduXcConnConfigProtected=oduXcConnConfigProtected, slXpdrTraps0=slXpdrTraps0, xpdrConnAddMask1=xpdrConnAddMask1, tribXcConnConfigP1=tribXcConnConfigP1, tribXcConnMask2=tribXcConnMask2, xpdrServiceType=xpdrServiceType, oduXcConnConfigEntry=oduXcConnConfigEntry, tribXcConnMask1=tribXcConnMask1, slXpdrLastChange=slXpdrLastChange, smmOwnerMode=smmOwnerMode, slXpdr=slXpdr, tribXcConnConfigTable=tribXcConnConfigTable, tribXcConnServiceType=tribXcConnServiceType, xpdrConnConfigCpriRateControl=xpdrConnConfigCpriRateControl, xpdrConnConfigTableChange0=xpdrConnConfigTableChange0, oduXcConnConfigP1=oduXcConnConfigP1, xpdrFecMode=xpdrFecMode, tribXcConnConfigProtected=tribXcConnConfigProtected, tribXcConnConfigRowStatus=tribXcConnConfigRowStatus, xpdrConnConfigRateControlOper=xpdrConnConfigRateControlOper, oduXcConnConfigRowStatus=oduXcConnConfigRowStatus, xpdrConnConfigIf1=xpdrConnConfigIf1, XpdrServiceType=XpdrServiceType, TsMaskBits=TsMaskBits, xpdrConnConfigRateControlAdmin=xpdrConnConfigRateControlAdmin, xpdrConnConfigTable=xpdrConnConfigTable, PYSNMP_MODULE_ID=slXpdr)
