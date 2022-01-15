#
# PySNMP MIB module ExaltComm-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/ExaltComm-TRAPS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
modelName, locLinkState, productsMIBNotifications = mibBuilder.importSymbols("ExaltComProducts", "modelName", "locLinkState", "productsMIBNotifications")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, TimeTicks, Counter64, Integer32, Counter32, iso, ModuleIdentity, MibIdentifier, Bits, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "TimeTicks", "Counter64", "Integer32", "Counter32", "iso", "ModuleIdentity", "MibIdentifier", "Bits", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
notifs = MibIdentifier((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1))
notifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2))
locRadioStat = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locRadioStat.setStatus('current')
if mibBuilder.loadTexts: locRadioStat.setDescription('This integer object reports for possible values:\n\t 0 for GREEN, 1 for YELLOW, 2 for RED, 3 for GRAY')
remRadioStat = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: remRadioStat.setStatus('current')
if mibBuilder.loadTexts: remRadioStat.setDescription('This integer object reports for possible values:\n\t 0 for GREEN, 1 for YELLOW, 2 for RED, 3 for GRAY')
locRSLStat = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locRSLStat.setStatus('current')
if mibBuilder.loadTexts: locRSLStat.setDescription('This integer object reports for possible values:\n\t 1 for high, 2 for low, 3 for normal')
locTempStat = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locTempStat.setStatus('current')
if mibBuilder.loadTexts: locTempStat.setDescription('This integer object reports for possible values:\n\t 1 for high, 2 for low, 3 for normal')
locRSLStatVert = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locRSLStatVert.setStatus('current')
if mibBuilder.loadTexts: locRSLStatVert.setDescription('This integer object reports for possible values:\n\t 1 for high, 2 for low, 3 for normal')
locEthWtmkHitDurationETH1 = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locEthWtmkHitDurationETH1.setStatus('current')
if mibBuilder.loadTexts: locEthWtmkHitDurationETH1.setDescription('Reports number of minutes passed since previons notification of Ethernet Utilization above watermark (ETH1)')
locEthWtmkHitDurationETH2 = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locEthWtmkHitDurationETH2.setStatus('current')
if mibBuilder.loadTexts: locEthWtmkHitDurationETH2.setDescription('Reports number of minutes passed since previons notification of Ethernet Utilization above watermark (ETH2)')
locEthWtmkHitDurationETH3 = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locEthWtmkHitDurationETH3.setStatus('current')
if mibBuilder.loadTexts: locEthWtmkHitDurationETH3.setDescription('Reports number of minutes passed since previons notification of Ethernet Utilization above watermark (ETH3)')
locEthWtmkHitDurationETH4 = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locEthWtmkHitDurationETH4.setStatus('current')
if mibBuilder.loadTexts: locEthWtmkHitDurationETH4.setDescription('Reports number of minutes passed since previons notification of Ethernet Utilization above watermark (ETH4)')
locRSLStatHoriz = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 10), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locRSLStatHoriz.setStatus('current')
if mibBuilder.loadTexts: locRSLStatHoriz.setDescription('This integer object reports for possible values: 1 for high, 2 for low, 3 for normal')
cold_start_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 1)).setLabel("cold-start-notif").setObjects(("ExaltComProducts", "modelName"))
if mibBuilder.loadTexts: cold_start_notif.setStatus('current')
if mibBuilder.loadTexts: cold_start_notif.setDescription('cold start Trap')
radio_syn_alm_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 2)).setLabel("radio-syn-alm-notif").setObjects(("ExaltComProducts", "locLinkState"))
if mibBuilder.loadTexts: radio_syn_alm_notif.setStatus('current')
if mibBuilder.loadTexts: radio_syn_alm_notif.setDescription('Local Link State Trap')
loc_radio_stat_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 3)).setLabel("loc-radio-stat-notif").setObjects(("ExaltComm-TRAPS-MIB", "locRadioStat"))
if mibBuilder.loadTexts: loc_radio_stat_notif.setStatus('current')
if mibBuilder.loadTexts: loc_radio_stat_notif.setDescription('Local Radio Status Trap')
rem_radio_stat_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 4)).setLabel("rem-radio-stat-notif").setObjects(("ExaltComm-TRAPS-MIB", "remRadioStat"))
if mibBuilder.loadTexts: rem_radio_stat_notif.setStatus('current')
if mibBuilder.loadTexts: rem_radio_stat_notif.setDescription('Remote Radio Status Trap')
loc_rsl_stat_horiz_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 5)).setLabel("loc-rsl-stat-horiz-notif").setObjects(("ExaltComm-TRAPS-MIB", "locRSLStatHoriz"))
if mibBuilder.loadTexts: loc_rsl_stat_horiz_notif.setStatus('current')
if mibBuilder.loadTexts: loc_rsl_stat_horiz_notif.setDescription('Local Horizontal RSL Event Trap')
loc_temp_stat_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 6)).setLabel("loc-temp-stat-notif").setObjects(("ExaltComm-TRAPS-MIB", "locTempStat"))
if mibBuilder.loadTexts: loc_temp_stat_notif.setStatus('current')
if mibBuilder.loadTexts: loc_temp_stat_notif.setDescription('Local Temperature Event Trap')
loc_rsl_stat_vert_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 7)).setLabel("loc-rsl-stat-vert-notif").setObjects(("ExaltComm-TRAPS-MIB", "locRSLStatVert"))
if mibBuilder.loadTexts: loc_rsl_stat_vert_notif.setStatus('current')
if mibBuilder.loadTexts: loc_rsl_stat_vert_notif.setDescription('Local Vertical RSL Event Trap')
chan_syn_alm_v_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 8)).setLabel("chan-syn-alm-v-notif").setObjects(("ExaltComProducts", "locLinkState"))
if mibBuilder.loadTexts: chan_syn_alm_v_notif.setStatus('current')
if mibBuilder.loadTexts: chan_syn_alm_v_notif.setDescription('Local Vertical Link State Trap')
chan_syn_alm_h_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 9)).setLabel("chan-syn-alm-h-notif").setObjects(("ExaltComProducts", "locLinkState"))
if mibBuilder.loadTexts: chan_syn_alm_h_notif.setStatus('current')
if mibBuilder.loadTexts: chan_syn_alm_h_notif.setDescription('Local Horizontal Link State Trap')
loc_rsl_stat_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 10)).setLabel("loc-rsl-stat-notif").setObjects(("ExaltComm-TRAPS-MIB", "locRSLStat"))
if mibBuilder.loadTexts: loc_rsl_stat_notif.setStatus('current')
if mibBuilder.loadTexts: loc_rsl_stat_notif.setDescription('Local RSL Event Trap')
eth_watermark_hit_duration_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 11)).setLabel("eth-watermark-hit-duration-notif").setObjects(("ExaltComm-TRAPS-MIB", "locEthWtmkHitDurationETH1"), ("ExaltComm-TRAPS-MIB", "locEthWtmkHitDurationETH2"), ("ExaltComm-TRAPS-MIB", "locEthWtmkHitDurationETH3"))
if mibBuilder.loadTexts: eth_watermark_hit_duration_notif.setStatus('current')
if mibBuilder.loadTexts: eth_watermark_hit_duration_notif.setDescription('Ethernet Utilization above watermark minutes Trap')
mibBuilder.exportSymbols("ExaltComm-TRAPS-MIB", radio_syn_alm_notif=radio_syn_alm_notif, cold_start_notif=cold_start_notif, notifObjects=notifObjects, locRSLStatVert=locRSLStatVert, notifs=notifs, loc_radio_stat_notif=loc_radio_stat_notif, chan_syn_alm_v_notif=chan_syn_alm_v_notif, loc_rsl_stat_notif=loc_rsl_stat_notif, eth_watermark_hit_duration_notif=eth_watermark_hit_duration_notif, locEthWtmkHitDurationETH4=locEthWtmkHitDurationETH4, loc_rsl_stat_vert_notif=loc_rsl_stat_vert_notif, remRadioStat=remRadioStat, locRSLStat=locRSLStat, locEthWtmkHitDurationETH2=locEthWtmkHitDurationETH2, locRadioStat=locRadioStat, locRSLStatHoriz=locRSLStatHoriz, chan_syn_alm_h_notif=chan_syn_alm_h_notif, locEthWtmkHitDurationETH3=locEthWtmkHitDurationETH3, loc_rsl_stat_horiz_notif=loc_rsl_stat_horiz_notif, rem_radio_stat_notif=rem_radio_stat_notif, loc_temp_stat_notif=loc_temp_stat_notif, locTempStat=locTempStat, locEthWtmkHitDurationETH1=locEthWtmkHitDurationETH1)
