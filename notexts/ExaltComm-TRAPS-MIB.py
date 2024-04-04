#
# PySNMP MIB module ExaltComm-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/ExaltComm-TRAPS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:54 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
productsMIBNotifications, modelName, locLinkState = mibBuilder.importSymbols("ExaltComProducts", "productsMIBNotifications", "modelName", "locLinkState")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Counter32, Counter64, NotificationType, Integer32, MibIdentifier, iso, IpAddress, TimeTicks, Gauge32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Counter32", "Counter64", "NotificationType", "Integer32", "MibIdentifier", "iso", "IpAddress", "TimeTicks", "Gauge32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
notifs = MibIdentifier((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1))
notifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2))
locRadioStat = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locRadioStat.setStatus('current')
remRadioStat = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: remRadioStat.setStatus('current')
locRSLStat = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locRSLStat.setStatus('current')
locTempStat = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locTempStat.setStatus('current')
locRSLStatVert = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locRSLStatVert.setStatus('current')
locEthWtmkHitDurationETH1 = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locEthWtmkHitDurationETH1.setStatus('current')
locEthWtmkHitDurationETH2 = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locEthWtmkHitDurationETH2.setStatus('current')
locEthWtmkHitDurationETH3 = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locEthWtmkHitDurationETH3.setStatus('current')
locEthWtmkHitDurationETH4 = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locEthWtmkHitDurationETH4.setStatus('current')
locRSLStatHoriz = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 10), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: locRSLStatHoriz.setStatus('current')
cold_start_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 1)).setLabel("cold-start-notif").setObjects(("ExaltComProducts", "modelName"))
if mibBuilder.loadTexts: cold_start_notif.setStatus('current')
radio_syn_alm_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 2)).setLabel("radio-syn-alm-notif").setObjects(("ExaltComProducts", "locLinkState"))
if mibBuilder.loadTexts: radio_syn_alm_notif.setStatus('current')
loc_radio_stat_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 3)).setLabel("loc-radio-stat-notif").setObjects(("ExaltComm-TRAPS-MIB", "locRadioStat"))
if mibBuilder.loadTexts: loc_radio_stat_notif.setStatus('current')
rem_radio_stat_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 4)).setLabel("rem-radio-stat-notif").setObjects(("ExaltComm-TRAPS-MIB", "remRadioStat"))
if mibBuilder.loadTexts: rem_radio_stat_notif.setStatus('current')
loc_rsl_stat_horiz_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 5)).setLabel("loc-rsl-stat-horiz-notif").setObjects(("ExaltComm-TRAPS-MIB", "locRSLStatHoriz"))
if mibBuilder.loadTexts: loc_rsl_stat_horiz_notif.setStatus('current')
loc_temp_stat_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 6)).setLabel("loc-temp-stat-notif").setObjects(("ExaltComm-TRAPS-MIB", "locTempStat"))
if mibBuilder.loadTexts: loc_temp_stat_notif.setStatus('current')
loc_rsl_stat_vert_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 7)).setLabel("loc-rsl-stat-vert-notif").setObjects(("ExaltComm-TRAPS-MIB", "locRSLStatVert"))
if mibBuilder.loadTexts: loc_rsl_stat_vert_notif.setStatus('current')
chan_syn_alm_v_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 8)).setLabel("chan-syn-alm-v-notif").setObjects(("ExaltComProducts", "locLinkState"))
if mibBuilder.loadTexts: chan_syn_alm_v_notif.setStatus('current')
chan_syn_alm_h_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 9)).setLabel("chan-syn-alm-h-notif").setObjects(("ExaltComProducts", "locLinkState"))
if mibBuilder.loadTexts: chan_syn_alm_h_notif.setStatus('current')
loc_rsl_stat_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 10)).setLabel("loc-rsl-stat-notif").setObjects(("ExaltComm-TRAPS-MIB", "locRSLStat"))
if mibBuilder.loadTexts: loc_rsl_stat_notif.setStatus('current')
eth_watermark_hit_duration_notif = NotificationType((1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 11)).setLabel("eth-watermark-hit-duration-notif").setObjects(("ExaltComm-TRAPS-MIB", "locEthWtmkHitDurationETH1"), ("ExaltComm-TRAPS-MIB", "locEthWtmkHitDurationETH2"), ("ExaltComm-TRAPS-MIB", "locEthWtmkHitDurationETH3"))
if mibBuilder.loadTexts: eth_watermark_hit_duration_notif.setStatus('current')
mibBuilder.exportSymbols("ExaltComm-TRAPS-MIB", cold_start_notif=cold_start_notif, radio_syn_alm_notif=radio_syn_alm_notif, rem_radio_stat_notif=rem_radio_stat_notif, loc_rsl_stat_notif=loc_rsl_stat_notif, remRadioStat=remRadioStat, locEthWtmkHitDurationETH1=locEthWtmkHitDurationETH1, locEthWtmkHitDurationETH3=locEthWtmkHitDurationETH3, locEthWtmkHitDurationETH2=locEthWtmkHitDurationETH2, locEthWtmkHitDurationETH4=locEthWtmkHitDurationETH4, loc_rsl_stat_vert_notif=loc_rsl_stat_vert_notif, locTempStat=locTempStat, notifObjects=notifObjects, locRSLStatHoriz=locRSLStatHoriz, locRSLStat=locRSLStat, chan_syn_alm_h_notif=chan_syn_alm_h_notif, notifs=notifs, locRadioStat=locRadioStat, eth_watermark_hit_duration_notif=eth_watermark_hit_duration_notif, loc_temp_stat_notif=loc_temp_stat_notif, chan_syn_alm_v_notif=chan_syn_alm_v_notif, locRSLStatVert=locRSLStatVert, loc_radio_stat_notif=loc_radio_stat_notif, loc_rsl_stat_horiz_notif=loc_rsl_stat_horiz_notif)
