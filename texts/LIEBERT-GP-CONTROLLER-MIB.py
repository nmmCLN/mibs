#
# PySNMP MIB module LIEBERT-GP-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-CONTROLLER-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:23:58 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
lgpController, liebertControllerModuleReg = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "lgpController", "liebertControllerModuleReg")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, IpAddress, Counter64, ModuleIdentity, Gauge32, Bits, Counter32, MibIdentifier, Integer32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "IpAddress", "Counter64", "ModuleIdentity", "Gauge32", "Bits", "Counter32", "MibIdentifier", "Integer32", "iso", "TimeTicks")
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
mibBuilder.exportSymbols("LIEBERT-GP-CONTROLLER-MIB", lgpCtrlBoardBatteryVoltage=lgpCtrlBoardBatteryVoltage, lgpCtrlNumberRedundantControlModules=lgpCtrlNumberRedundantControlModules, lgpCtrlNumberControlModuleWarnings=lgpCtrlNumberControlModuleWarnings, liebertControllerModule=liebertControllerModule, lgpCtrlNumberInstalledControlModules=lgpCtrlNumberInstalledControlModules, PYSNMP_MODULE_ID=liebertControllerModule, lgpCtrlNumberFailedControlModules=lgpCtrlNumberFailedControlModules)
