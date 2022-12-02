#
# PySNMP MIB module LIEBERT-GP-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-CONTROLLER-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 17:11:12 2022
# On host fv-az563-842 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
liebertControllerModuleReg, lgpController = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "liebertControllerModuleReg", "lgpController")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, MibIdentifier, Gauge32, IpAddress, ModuleIdentity, Counter64, Unsigned32, TimeTicks, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibIdentifier", "Gauge32", "IpAddress", "ModuleIdentity", "Counter64", "Unsigned32", "TimeTicks", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
liebertControllerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 7, 1))
liebertControllerModule.setRevisions(('2008-07-02 00:00', '2008-01-10 00:00', '2006-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: liebertControllerModule.setRevisionsDescriptions(('Removed unnecessary item from import statement', 'Modified contact email address.', 'Added support for Liebert DS Unit.',))
if mibBuilder.loadTexts: liebertControllerModule.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: liebertControllerModule.setOrganization('Liebert Corporation')
if mibBuilder.loadTexts: liebertControllerModule.setContactInfo('Contact:   Technical Support\n\n      Postal:\n      Liebert Corporation\n      1050 Dearborn Drive\n      P.O. Box 29186\n      Columbus OH, 43229\n      US\n\n      Tel: +1 (800) 222-5877\n\n      E-mail: liebert.monitoring@vertivco.com\n      Web:    www.vertivco.com\n\n      Author:  Gregory M. Hoge')
if mibBuilder.loadTexts: liebertControllerModule.setDescription("The MIB module used to specify Liebert Controller OIDs\n\n      Copyright 2000-2008 Liebert Corporation. All rights reserved.\n      Reproduction of this document is authorized on the condition\n      that the forgoing copyright notice is included.\n\n      This Specification is supplied 'AS IS' and Liebert Corporation\n      makes no warranty, either express or implied, as to the use,\n      operation, condition, or performance of the Specification.")
lgpCtrlNumberInstalledControlModules = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberInstalledControlModules.setStatus('current')
if mibBuilder.loadTexts: lgpCtrlNumberInstalledControlModules.setDescription('The number of control modules installed in the device.')
lgpCtrlNumberFailedControlModules = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberFailedControlModules.setStatus('current')
if mibBuilder.loadTexts: lgpCtrlNumberFailedControlModules.setDescription('The number of control modules in the device that have failed.')
lgpCtrlNumberRedundantControlModules = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberRedundantControlModules.setStatus('current')
if mibBuilder.loadTexts: lgpCtrlNumberRedundantControlModules.setDescription('The number of redundant control modules installed in the device.')
lgpCtrlNumberControlModuleWarnings = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberControlModuleWarnings.setStatus('current')
if mibBuilder.loadTexts: lgpCtrlNumberControlModuleWarnings.setDescription('The number of control modules in the device that have a warning.')
lgpCtrlBoardBatteryVoltage = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 6), Unsigned32()).setUnits('.01 Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlBoardBatteryVoltage.setStatus('current')
if mibBuilder.loadTexts: lgpCtrlBoardBatteryVoltage.setDescription('The control board battery voltage.  Typically this battery is used\n        to provide backup power to memory and other vital circuits.')
mibBuilder.exportSymbols("LIEBERT-GP-CONTROLLER-MIB", lgpCtrlNumberRedundantControlModules=lgpCtrlNumberRedundantControlModules, lgpCtrlNumberFailedControlModules=lgpCtrlNumberFailedControlModules, PYSNMP_MODULE_ID=liebertControllerModule, lgpCtrlBoardBatteryVoltage=lgpCtrlBoardBatteryVoltage, liebertControllerModule=liebertControllerModule, lgpCtrlNumberInstalledControlModules=lgpCtrlNumberInstalledControlModules, lgpCtrlNumberControlModuleWarnings=lgpCtrlNumberControlModuleWarnings)
