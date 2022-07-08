#
# PySNMP MIB module IANA-LANGUAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-LANGUAGE-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:11:27 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, Gauge32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, NotificationType, mib_2, Integer32, TimeTicks, Bits, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "NotificationType", "mib-2", "Integer32", "TimeTicks", "Bits", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaLanguages = ModuleIdentity((1, 3, 6, 1, 2, 1, 73))
ianaLanguages.setRevisions(('2014-05-22 00:00', '2000-05-10 00:00', '1999-09-09 09:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaLanguages.setRevisionsDescriptions(('Updated contact info.', 'Import mib-2 instead of experimental, so that\n                 this module compiles', 'Initial version as published at time of\n                 publication of RFC 2591.',))
if mibBuilder.loadTexts: ianaLanguages.setLastUpdated('201405220000Z')
if mibBuilder.loadTexts: ianaLanguages.setOrganization('IANA')
if mibBuilder.loadTexts: ianaLanguages.setContactInfo('Internet Assigned Numbers Authority (IANA)\n\n         Postal: ICANN\n                 12025 Waterfront Drive, Suite 300\n                 Los Angeles, CA 90094-2536\n\n         Tel:    +1 310-301-5800\n         E-Mail: iana&iana.org')
if mibBuilder.loadTexts: ianaLanguages.setDescription("The MIB module registers object identifier values for\n         well-known programming and scripting languages. Every\n         language registration MUST describe the format used\n         when transferring scripts written in this language.\n\n         Any additions or changes to the contents of this MIB\n         module require Designated Expert Review as defined in\n         the Guidelines for Writing IANA Considerations Section\n         document. The Designated Expert will be selected by\n         the IESG Area Director of the OPS Area.\n\n         Note, this module does not have to register all possible\n         languages since languages are identified by object\n         identifier values. It is therefore possible to registered\n         languages in private OID trees. The references given below are not\n         normative with regard to the language version. Other\n         references might be better suited to describe some newer\n         versions of this language. The references are only\n         provided as `a pointer into the right direction'.")
ianaLangJavaByteCode = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 1))
if mibBuilder.loadTexts: ianaLangJavaByteCode.setStatus('current')
if mibBuilder.loadTexts: ianaLangJavaByteCode.setDescription('Java byte code to be processed by a Java virtual machine.\n         A script written in Java byte code is transferred by using\n         the Java archive file format (JAR).')
if mibBuilder.loadTexts: ianaLangJavaByteCode.setReference('The Java Virtual Machine Specification.\n         ISBN 0-201-63452-X')
ianaLangTcl = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 2))
if mibBuilder.loadTexts: ianaLangTcl.setStatus('current')
if mibBuilder.loadTexts: ianaLangTcl.setDescription('The Tool Command Language (Tcl). A script written in the\n         Tcl language is transferred in Tcl source code format.')
if mibBuilder.loadTexts: ianaLangTcl.setReference('Tcl and the Tk Toolkit.\n         ISBN 0-201-63337-X')
ianaLangPerl = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 3))
if mibBuilder.loadTexts: ianaLangPerl.setStatus('current')
if mibBuilder.loadTexts: ianaLangPerl.setDescription('The Perl language. A script written in the Perl language\n         is transferred in Perl source code format.')
if mibBuilder.loadTexts: ianaLangPerl.setReference('Programming Perl.\n         ISBN 1-56592-149-6')
ianaLangScheme = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 4))
if mibBuilder.loadTexts: ianaLangScheme.setStatus('current')
if mibBuilder.loadTexts: ianaLangScheme.setDescription('The Scheme language. A script written in the Scheme\n         language is transferred in Scheme source code format.')
if mibBuilder.loadTexts: ianaLangScheme.setReference('The Revised^4 Report on the Algorithmic Language Scheme.\n         MIT Press')
ianaLangSRSL = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 5))
if mibBuilder.loadTexts: ianaLangSRSL.setStatus('current')
if mibBuilder.loadTexts: ianaLangSRSL.setDescription('The SNMP Script Language defined by SNMP Research. A\n         script written in the SNMP Script Language is transferred\n         in the SNMP Script Language source code format.')
ianaLangPSL = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 6))
if mibBuilder.loadTexts: ianaLangPSL.setStatus('current')
if mibBuilder.loadTexts: ianaLangPSL.setDescription('The Patrol Script Language defined by BMC Software. A script\n         written in the Patrol Script Language is transferred in the\n         Patrol Script Language source code format.')
if mibBuilder.loadTexts: ianaLangPSL.setReference('PATROL Script Language Reference Manual, Version 3.0,\n         November 30, 1995. BMC Software, Inc. 2101 City West Blvd.,\n         Houston, Texas 77042.')
ianaLangSMSL = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 7))
if mibBuilder.loadTexts: ianaLangSMSL.setStatus('current')
if mibBuilder.loadTexts: ianaLangSMSL.setDescription('The Systems Management Scripting Language. A script written\n         in the SMSL language is transferred in the SMSL source code\n         format.')
if mibBuilder.loadTexts: ianaLangSMSL.setReference('ISO/ITU Command Sequencer.\n         ISO 10164-21 or ITU X.753')
mibBuilder.exportSymbols("IANA-LANGUAGE-MIB", ianaLanguages=ianaLanguages, ianaLangPSL=ianaLangPSL, ianaLangJavaByteCode=ianaLangJavaByteCode, ianaLangSMSL=ianaLangSMSL, ianaLangTcl=ianaLangTcl, ianaLangSRSL=ianaLangSRSL, PYSNMP_MODULE_ID=ianaLanguages, ianaLangScheme=ianaLangScheme, ianaLangPerl=ianaLangPerl)
