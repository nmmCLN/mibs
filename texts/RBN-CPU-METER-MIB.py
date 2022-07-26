#
# PySNMP MIB module RBN-CPU-METER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-CPU-METER-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:50 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnPercentage, = mibBuilder.importSymbols("RBN-TC", "RbnPercentage")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, Integer32, ObjectIdentity, MibIdentifier, Gauge32, Counter64, TimeTicks, IpAddress, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "Integer32", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter64", "TimeTicks", "IpAddress", "ModuleIdentity", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnCpuMeterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 6))
rbnCpuMeterMIB.setRevisions(('2011-12-13 18:00', '2011-01-19 18:00', '2002-12-16 00:00', '2002-06-26 00:00', '2002-05-29 00:00', '1999-06-16 23:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnCpuMeterMIB.setRevisionsDescriptions(('Added rbnCpuMeterFiveSecondPeak, rbnCpuMeterOneMinutePeak, and\n        rbnCpuMeterFiveMinutePeak to monitor system peak CPU usage. Updated\n        conformance information.', 'Update CONTACT-INFO & ORGANIZATION. Corrected max length of\n        rbnCpuProcName', 'Added a per process table to monitor the cpu usage of\n         each of the processes on the system.', 'Updated CONTACT-INFO. Deprecated TEXTUAL-CONVENTION: Percentage.  \n        Use RbnPercentage in SYNTAX.', 'Update/correct CONTACT-INFO. Fix syntax errors on IMPORTS list.', 'Creation of the CPU meter MIB.',))
if mibBuilder.loadTexts: rbnCpuMeterMIB.setLastUpdated('201112131800Z')
if mibBuilder.loadTexts: rbnCpuMeterMIB.setOrganization('Ericsson AB.')
if mibBuilder.loadTexts: rbnCpuMeterMIB.setContactInfo('       Ericsson AB.\n\n                Postal: 100 Headquarters Dr\n                        San Jose, CA 95134\n                        USA\n\n                 Phone: +1 408 750 5000\n                   Fax: +1 408 750 5599\n\n                ')
if mibBuilder.loadTexts: rbnCpuMeterMIB.setDescription('This management information module measures CPU \n                utilization on a device.')
rbnCpuMeterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1))
rbnCpuMeterMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2))
rbnCpuProcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3))
class Percentage(TextualConvention, Integer32):
    description = 'This Textual Convention describes an object that stores \n     a whole integer percentage value.'
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

rbnCpuMeterFiveSecondAvg = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 1), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterFiveSecondAvg.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterFiveSecondAvg.setDescription('Provides the CPU usage percentage over the first five\n                 second period in the scheduler.')
rbnCpuMeterOneMinuteAvg = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 2), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterOneMinuteAvg.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterOneMinuteAvg.setDescription('Provides a cumulative average of the CPU usage percentage\n                 over a one minute period.')
rbnCpuMeterFiveMinuteAvg = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 3), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterFiveMinuteAvg.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterFiveMinuteAvg.setDescription('Provides a cumulative average of the CPU usage percentage\n                 over a five minute period.')
rbnCpuMeterFiveSecondPeak = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 4), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterFiveSecondPeak.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterFiveSecondPeak.setDescription('The peak CPU usage percentage over the first five\n                 second period.')
rbnCpuMeterOneMinutePeak = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 5), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterOneMinutePeak.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterOneMinutePeak.setDescription('The peak CPU usage percentage over a one minute\n                 period.')
rbnCpuMeterFiveMinutePeak = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 6), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterFiveMinutePeak.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterFiveMinutePeak.setDescription('The peak CPU usage percentage over a five minute\n                 period.')
rbnCpuProcTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1), )
if mibBuilder.loadTexts: rbnCpuProcTable.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProcTable.setDescription('This table contains the objects which identify cpu processes.\n                With respect to creation and deletion of entries in this table,\n                rows in the table are created or deleted as processes are started \n                or terminated.')
rbnCpuProcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1), ).setIndexNames((1, "RBN-CPU-METER-MIB", "rbnCpuProcName"))
if mibBuilder.loadTexts: rbnCpuProcEntry.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProcEntry.setDescription('A conceptual row in the rbnCpuProcTable.')
rbnCpuProcName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 114))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProcName.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProcName.setDescription('The name for this process.')
rbnCpuProcPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProcPriority.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProcPriority.setDescription('The priority of this process. This value ranges \n                from 0 to 255, with 0 being the highest priority.')
rbnCpuProcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProcTime.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProcTime.setDescription('The total time, in milliseconds, that has been spent \n                in this process.')
rbnCpuProcCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProcCalls.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProcCalls.setDescription('The number of times that this process has acquired\n                 the cpu.')
rbnCpuProc5Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 5), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProc5Sec.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProc5Sec.setDescription('The average cpu usage in a 5 second window for this process.')
rbnCpuProc1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 6), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProc1Min.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProc1Min.setDescription('The average cpu usage in a 1 minute window for this process.')
rbnCpuProc5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 7), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProc5Min.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProc5Min.setDescription('The average cpu usage in a 5 minute window for this process.')
rbnCpuProcLongest = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProcLongest.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProcLongest.setDescription('The maximum time, in milliseconds, spent in this process.')
rbnCpuMeterMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 1))
rbnCpuMeterMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2))
rbnCpuProcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 3))
rbnCpuMeterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2, 1)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuMeterStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterMIBCompliance = rbnCpuMeterMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: rbnCpuMeterMIBCompliance.setDescription('The compliance statement for the CPU meter MIB.')
rbnCpuMeterMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2, 2)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuMeterStatsGroup"), ("RBN-CPU-METER-MIB", "rbnCpuProcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterMIBCompliance1 = rbnCpuMeterMIBCompliance1.setStatus('deprecated')
if mibBuilder.loadTexts: rbnCpuMeterMIBCompliance1.setDescription('The compliance statement for the CPU meter MIB\n                with added support for per process monitoring.')
rbnCpuMeterMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2, 3)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuMeterStatsGroup2"), ("RBN-CPU-METER-MIB", "rbnCpuProcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterMIBCompliance2 = rbnCpuMeterMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterMIBCompliance2.setDescription('The compliance statement for the CPU meter MIB\n                with added support for per process monitoring.')
rbnCpuMeterStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 1, 1)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuMeterFiveSecondAvg"), ("RBN-CPU-METER-MIB", "rbnCpuMeterOneMinuteAvg"), ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveMinuteAvg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterStatsGroup = rbnCpuMeterStatsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: rbnCpuMeterStatsGroup.setDescription('A collection of objects providing CPU utilization\n                 information.')
rbnCpuProcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 3, 1)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuProcName"), ("RBN-CPU-METER-MIB", "rbnCpuProcPriority"), ("RBN-CPU-METER-MIB", "rbnCpuProcTime"), ("RBN-CPU-METER-MIB", "rbnCpuProcCalls"), ("RBN-CPU-METER-MIB", "rbnCpuProc5Sec"), ("RBN-CPU-METER-MIB", "rbnCpuProc1Min"), ("RBN-CPU-METER-MIB", "rbnCpuProc5Min"), ("RBN-CPU-METER-MIB", "rbnCpuProcLongest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuProcGroup = rbnCpuProcGroup.setStatus('current')
if mibBuilder.loadTexts: rbnCpuProcGroup.setDescription('The collection of all objects used for monitoring cpu\n                utilization of each process.')
rbnCpuMeterStatsGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 1, 2)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuMeterFiveSecondAvg"), ("RBN-CPU-METER-MIB", "rbnCpuMeterOneMinuteAvg"), ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveMinuteAvg"), ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveSecondPeak"), ("RBN-CPU-METER-MIB", "rbnCpuMeterOneMinutePeak"), ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveMinutePeak"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterStatsGroup2 = rbnCpuMeterStatsGroup2.setStatus('current')
if mibBuilder.loadTexts: rbnCpuMeterStatsGroup2.setDescription('A collection of objects providing CPU utilization\n                information.')
mibBuilder.exportSymbols("RBN-CPU-METER-MIB", Percentage=Percentage, rbnCpuProcGroup=rbnCpuProcGroup, rbnCpuMeterOneMinutePeak=rbnCpuMeterOneMinutePeak, rbnCpuMeterStatsGroup=rbnCpuMeterStatsGroup, rbnCpuProc5Sec=rbnCpuProc5Sec, rbnCpuMeterMIBConformance=rbnCpuMeterMIBConformance, rbnCpuProc1Min=rbnCpuProc1Min, rbnCpuMeterMIBCompliance=rbnCpuMeterMIBCompliance, rbnCpuMeterMIB=rbnCpuMeterMIB, rbnCpuProcGroups=rbnCpuProcGroups, rbnCpuProcPriority=rbnCpuProcPriority, rbnCpuProc5Min=rbnCpuProc5Min, rbnCpuMeterFiveSecondAvg=rbnCpuMeterFiveSecondAvg, rbnCpuMeterMIBCompliance2=rbnCpuMeterMIBCompliance2, rbnCpuMeterStatsGroup2=rbnCpuMeterStatsGroup2, rbnCpuMeterFiveMinutePeak=rbnCpuMeterFiveMinutePeak, rbnCpuMeterMIBCompliance1=rbnCpuMeterMIBCompliance1, rbnCpuProcLongest=rbnCpuProcLongest, rbnCpuMeterOneMinuteAvg=rbnCpuMeterOneMinuteAvg, rbnCpuMeterFiveSecondPeak=rbnCpuMeterFiveSecondPeak, rbnCpuMeterMIBCompliances=rbnCpuMeterMIBCompliances, rbnCpuProcTable=rbnCpuProcTable, rbnCpuMeterFiveMinuteAvg=rbnCpuMeterFiveMinuteAvg, rbnCpuProcTime=rbnCpuProcTime, rbnCpuProcEntry=rbnCpuProcEntry, rbnCpuProcCalls=rbnCpuProcCalls, rbnCpuMeterMIBObjects=rbnCpuMeterMIBObjects, rbnCpuProcMIBObjects=rbnCpuProcMIBObjects, PYSNMP_MODULE_ID=rbnCpuMeterMIB, rbnCpuMeterMIBGroups=rbnCpuMeterMIBGroups, rbnCpuProcName=rbnCpuProcName)
