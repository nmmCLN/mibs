#
# PySNMP MIB module RBN-CPU-METER-CAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-CPU-METER-CAP
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:37 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
rbnCapabilities, = mibBuilder.importSymbols("RBN-SMI", "rbnCapabilities")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, TimeTicks, ModuleIdentity, NotificationType, MibIdentifier, ObjectIdentity, IpAddress, Counter64, Gauge32, Unsigned32, Bits, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "ModuleIdentity", "NotificationType", "MibIdentifier", "ObjectIdentity", "IpAddress", "Counter64", "Gauge32", "Unsigned32", "Bits", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnCpuMeterCap = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 4, 22))
rbnCpuMeterCap.setRevisions(('2011-12-13 18:00', '2011-06-15 00:00', '2010-11-01 00:00', '2003-10-14 00:00', '2003-07-07 00:00', '2003-02-11 00:00', '2002-06-26 00:00', '1999-06-16 23:00',))
if mibBuilder.loadTexts: rbnCpuMeterCap.setLastUpdated('201112131800Z')
if mibBuilder.loadTexts: rbnCpuMeterCap.setOrganization('Ericsson Inc.')
rbnCpuMeterCap1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap1 = rbnCpuMeterCap1.setProductRelease('AOS 3.0.X.X')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap1 = rbnCpuMeterCap1.setStatus('current')
rbnCpuMeterCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap2 = rbnCpuMeterCap2.setProductRelease('SEOS 2.3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap2 = rbnCpuMeterCap2.setStatus('current')
rbnCpuMeterCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap3 = rbnCpuMeterCap3.setProductRelease('AOS 6.0.X.X')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap3 = rbnCpuMeterCap3.setStatus('current')
rbnCpuMeterCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap4 = rbnCpuMeterCap4.setProductRelease('SEOS 2.5.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap4 = rbnCpuMeterCap4.setStatus('current')
rbnCpuMeterCap5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap5 = rbnCpuMeterCap5.setProductRelease('SEOS 2.6.3 [SE]; SEOS 6.3.X [SM]; SEOS 11.1.X [SSR]')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap5 = rbnCpuMeterCap5.setStatus('current')
rbnCpuMeterCap6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2352, 4, 22, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap6 = rbnCpuMeterCap6.setProductRelease('IPOS 11.2.X')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterCap6 = rbnCpuMeterCap6.setStatus('current')
mibBuilder.exportSymbols("RBN-CPU-METER-CAP", rbnCpuMeterCap5=rbnCpuMeterCap5, rbnCpuMeterCap6=rbnCpuMeterCap6, rbnCpuMeterCap4=rbnCpuMeterCap4, rbnCpuMeterCap1=rbnCpuMeterCap1, rbnCpuMeterCap3=rbnCpuMeterCap3, rbnCpuMeterCap=rbnCpuMeterCap, rbnCpuMeterCap2=rbnCpuMeterCap2, PYSNMP_MODULE_ID=rbnCpuMeterCap)
