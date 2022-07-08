#
# PySNMP MIB module CTRON-DOWNLOAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DOWNLOAD-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:30 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ctDownLoad, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDownLoad")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Unsigned32, ObjectIdentity, MibIdentifier, Gauge32, IpAddress, Bits, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Gauge32", "IpAddress", "Bits", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctDL = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1))
ctDLForceOnBoot = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLForceOnBoot.setStatus('obsolete')
ctDLCommitRAMToFlash = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLCommitRAMToFlash.setStatus('obsolete')
ctDLInitiateColdBoot = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLInitiateColdBoot.setStatus('mandatory')
ctDLTFTPRequestHost = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLTFTPRequestHost.setStatus('obsolete')
ctDLTFTPRequest = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLTFTPRequest.setStatus('obsolete')
ctDLLastImageFilename = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLLastImageFilename.setStatus('mandatory')
ctDLLastServerIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLLastServerIPAddress.setStatus('mandatory')
ctDLFlashSize = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLFlashSize.setStatus('obsolete')
ctDLFlashCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLFlashCount.setStatus('obsolete')
ctDLFirmwareBase = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLFirmwareBase.setStatus('obsolete')
ctDLFirmwareTop = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLFirmwareTop.setStatus('obsolete')
ctDLFirmwareStart = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLFirmwareStart.setStatus('obsolete')
ctDLBootRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(9, 9)).setFixedLength(9)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLBootRev.setStatus('obsolete')
ctDLForceBootp = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLForceBootp.setStatus('obsolete')
ctDLServerName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 15), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLServerName.setStatus('obsolete')
ctDLOnLineDownLoad = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normalOperation", 1), ("forceDownLoad", 2), ("forceDownLoadReset", 3), ("downLoadConfiguration", 4), ("upLoadConfiguration", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLOnLineDownLoad.setStatus('mandatory')
ctDLOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("normalOperation", 3), ("downLoadActive", 4), ("downLoadCompleteError", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLOperStatus.setStatus('mandatory')
ctDLNetAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLNetAddress.setStatus('mandatory')
ctDLFileName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLFileName.setStatus('mandatory')
ctDLErrorString = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLErrorString.setStatus('mandatory')
ctDLTftpServerGatewayIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 21), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDLTftpServerGatewayIPAddress.setStatus('obsolete')
ctDLBlockCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLBlockCount.setStatus('mandatory')
ctDLBootPartitionStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("good", 1), ("bad", 2), ("inProgress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDLBootPartitionStatus.setStatus('obsolete')
mibBuilder.exportSymbols("CTRON-DOWNLOAD-MIB", ctDLCommitRAMToFlash=ctDLCommitRAMToFlash, ctDLTFTPRequest=ctDLTFTPRequest, ctDLBootPartitionStatus=ctDLBootPartitionStatus, ctDLBlockCount=ctDLBlockCount, ctDLOnLineDownLoad=ctDLOnLineDownLoad, ctDLFlashCount=ctDLFlashCount, ctDLServerName=ctDLServerName, ctDLErrorString=ctDLErrorString, ctDLForceOnBoot=ctDLForceOnBoot, ctDLTFTPRequestHost=ctDLTFTPRequestHost, ctDLBootRev=ctDLBootRev, ctDLLastImageFilename=ctDLLastImageFilename, ctDL=ctDL, ctDLInitiateColdBoot=ctDLInitiateColdBoot, ctDLFirmwareBase=ctDLFirmwareBase, ctDLOperStatus=ctDLOperStatus, ctDLNetAddress=ctDLNetAddress, ctDLFirmwareStart=ctDLFirmwareStart, ctDLFirmwareTop=ctDLFirmwareTop, ctDLTftpServerGatewayIPAddress=ctDLTftpServerGatewayIPAddress, ctDLForceBootp=ctDLForceBootp, ctDLLastServerIPAddress=ctDLLastServerIPAddress, ctDLFlashSize=ctDLFlashSize, ctDLFileName=ctDLFileName)
