#
# PySNMP MIB module RADLAN-SNMPv2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SNMPv2
# Produced by pysmi-1.1.8 at Mon Jan  9 10:36:33 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, IpAddress, Counter64, Bits, iso, NotificationType, ObjectIdentity, Counter32, ModuleIdentity, MibIdentifier, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "IpAddress", "Counter64", "Bits", "iso", "NotificationType", "ObjectIdentity", "Counter32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class RowStatus(TextualConvention, Integer32):
    description = "The RowStatus textual convention is used to manage the\n            creation and deletion of conceptual rows, and is used as the\n            value of the SYNTAX clause for the status column of a\n            conceptual row (as described in Section 7.7.1 of [2].)\n\n            The status column has six defined values:\n\n                 - `active', which indicates that the conceptual row is\n                 available for use by the managed device;\n\n                 - `notInService', which indicates that the conceptual\n                 row exists in the agent, but is unavailable for use by\n                 the managed device (see NOTE below); 'notInService' has\n                 no implication regarding the internal consistency of\n                 the row, availability of resources, or consistency with\n                 the current state of the managed device;\n\n                 - `notReady', which indicates that the conceptual row\n                 exists in the agent, but is missing information\n                 necessary in order to be available for use by the\n                 managed device (i.e., one or more required columns in\n                 the conceptual row have not been instanciated);\n\n                 - `createAndGo', which is supplied by a management\n                 station wishing to create a new instance of a\n                 conceptual row and to have its status automatically set\n                 to active, making it available for use by the managed\n                 device;\n\n                 - `createAndWait', which is supplied by a management\n                 station wishing to create a new instance of a\n                 conceptual row (but not make it available for use by\n                 the managed device); and,\n\n                 - `destroy', which is supplied by a management station\n                 wishing to delete all of the instances associated with\n                 an existing conceptual row.\n\n            Whereas five of the six values (all except `notReady') may\n            be specified in a management protocol set operation, only\n            three values will be returned in response to a management\n            protocol retrieval operation: `notReady', `notInService' or\n            `active'.  That is, when queried, an existing conceptual row\n            has only three states: it is either available for use by the\n            managed device (the status column has value `active'); it is\n            not available for use by the managed device, though the\n            agent has sufficient information to attempt to make it so\n            (the status column has value `notInService'); or, it is not\n            available for use by the managed device, and an attempt to\n            make it so would fail because the agent has insufficient\n            information (the state column has value `notReady').\n\n                                     NOTE WELL\n\n                 This textual convention may be used for a MIB table,\n                 irrespective of whether the values of that table's\n                 conceptual rows are able to be modified while it is\n                 active, or whether its conceptual rows must be taken\n                 out of service in order to be modified.  That is, it is\n                 the responsibility of the DESCRIPTION clause of the\n                 status column to specify whether the status column must\n                 not be `active' in order for the value of some other\n                 column of the same conceptual row to be modified.  If\n                 such a specification is made, affected columns may be\n                 changed by an SNMP set PDU if the RowStatus would not\n                 be equal to `active' either immediately before or after\n                 processing the PDU.  In other words, if the PDU also\n                 contained a varbind that would change the RowStatus\n                 value, the column in question may be changed if the\n                 RowStatus was not equal to `active' as the PDU was\n                 received, or if the varbind sets the status to a value\n                 other than 'active'.\n\n            Also note that whenever any elements of a row exist, the\n            RowStatus column must also exist.\n\n            To summarize the effect of having a conceptual row with a\n            status column having a SYNTAX clause value of RowStatus,\n            consider the following state diagram:\n\n\n                                         STATE\n              +--------------+-----------+-------------+-------------\n              |      A       |     B     |      C      |      D\n              |              |status col.|status column|\n              |status column |    is     |      is     |status column\n    ACTION    |does not exist|  notReady | notInService|  is active\n--------------+--------------+-----------+-------------+-------------\nset status    |noError    ->D|inconsist- |inconsistent-|inconsistent-\ncolumn to     |       or     |   entValue|        Value|        Value\ncreateAndGo   |inconsistent- |           |             |\n              |         Value|           |             |\n--------------+--------------+-----------+-------------+-------------\nset status    |noError  see 1|inconsist- |inconsistent-|inconsistent-\ncolumn to     |       or     |   entValue|        Value|        Value\ncreateAndWait |wrongValue    |           |             |\n--------------+--------------+-----------+-------------+-------------\nset status    |inconsistent- |inconsist- |noError      |noError\ncolumn to     |         Value|   entValue|             |\nactive        |              |           |             |\n              |              |     or    |             |\n              |              |           |             |\n              |              |see 2   ->D|see 8     ->D|          ->D\n--------------+--------------+-----------+-------------+-------------\nset status    |inconsistent- |inconsist- |noError      |noError   ->C\ncolumn to     |         Value|   entValue|             |\nnotInService  |              |           |             |\n              |              |     or    |             |      or\n              |              |           |             |\n              |              |see 3   ->C|          ->C|see 6\n--------------+--------------+-----------+-------------+-------------\nset status    |noError       |noError    |noError      |noError   ->A\ncolumn to     |              |           |             |      or\ndestroy       |           ->A|        ->A|          ->A|see 7\n--------------+--------------+-----------+-------------+-------------\nset any other |see 4         |noError    |noError      |see 5\ncolumn to some|              |           |             |\nvalue         |              |      see 1|          ->C|          ->D\n--------------+--------------+-----------+-------------+-------------\n\n    (1) goto B or C, depending on information available to the\n    agent.\n\n    (2) if other variable bindings included in the same PDU,\n    provide values for all columns which are missing but\n    required, and all columns have acceptable values, then\n    return noError and goto D.\n\n    (3) if other variable bindings included in the same PDU,\n    provide legal values for all columns which are missing but\n    required, then return noError and goto C.\n\n    (4) at the discretion of the agent, the return value may be\n    either:\n\n         inconsistentName: because the agent does not choose to\n         create such an instance when the corresponding\n         RowStatus instance does not exist, or\n\n         inconsistentValue: if the supplied value is\n         inconsistent with the state of some other MIB object's\n         value, or\n\n         noError: because the agent chooses to create the\n         instance.\n\n    If noError is returned, then the instance of the status\n    column must also be created, and the new state is B or C,\n    depending on the information available to the agent.  If\n    inconsistentName or inconsistentValue is returned, the row\n    remains in state A.\n\n    (5) depending on the MIB definition for the column/table,\n    either noError or inconsistentValue may be returned.\n\n    (6) the return value can indicate one of the following\n    errors:\n\n         wrongValue: because the agent does not support\n         notInService (e.g., an agent which does not support\n         createAndWait), or\n\n         inconsistentValue: because the agent is unable to take\n         the row out of service at this time, perhaps because it\n         is in use and cannot be de-activated.\n\n    (7) the return value can indicate the following error:\n\n         inconsistentValue: because the agent is unable to\n         remove the row at this time, perhaps because it is in\n         use and cannot be de-activated.\n\n    (8) the transition to D can fail, e.g., if the values of the\n    conceptual row are inconsistent, then the error code would\n    be inconsistentValue.\n\n    NOTE: Other processing of (this and other varbinds of) the\n    set request may result in a response other than noError\n    being returned, e.g., wrongValue, noCreation, etc.\n\n\n                      Conceptual Row Creation\n\n    There are four potential interactions when creating a\n    conceptual row: selecting an instance-identifier which is\n    not in use; creating the conceptual row; initializing any\n    objects for which the agent does not supply a default; and,\n    making the conceptual row available for use by the managed\n    device.\n\n    Interaction 1: Selecting an Instance-Identifier\n\n    The algorithm used to select an instance-identifier varies\n    for each conceptual row.  In some cases, the instance-\n    identifier is semantically significant, e.g., the\n    destination address of a route, and a management station\n    selects the instance-identifier according to the semantics.\n\n    In other cases, the instance-identifier is used solely to\n    distinguish conceptual rows, and a management station\n    without specific knowledge of the conceptual row might\n    examine the instances present in order to determine an\n    unused instance-identifier.  (This approach may be used, but\n    it is often highly sub-optimal; however, it is also a\n    questionable practice for a naive management station to\n    attempt conceptual row creation.)\n\n    Alternately, the MIB module which defines the conceptual row\n    might provide one or more objects which provide assistance\n    in determining an unused instance-identifier.  For example,\n    if the conceptual row is indexed by an integer-value, then\n    an object having an integer-valued SYNTAX clause might be\n    defined for such a purpose, allowing a management station to\n    issue a management protocol retrieval operation.  In order\n    to avoid unnecessary collisions between competing management\n    stations, `adjacent' retrievals of this object should be\n    different.\n\n    Finally, the management station could select a pseudo-random\n    number to use as the index.  In the event that this index\n    was already in use and an inconsistentValue was returned in\n    response to the management protocol set operation, the\n    management station should simply select a new pseudo-random\n    number and retry the operation.\n\n    A MIB designer should choose between the two latter\n    algorithms based on the size of the table (and therefore the\n    efficiency of each algorithm).  For tables in which a large\n    number of entries are expected, it is recommended that a MIB\n    object be defined that returns an acceptable index for\n    creation.  For tables with small numbers of entries, it is\n    recommended that the latter pseudo-random index mechanism be\n    used.\n\n    Interaction 2: Creating the Conceptual Row\n\n    Once an unused instance-identifier has been selected, the\n    management station determines if it wishes to create and\n    activate the conceptual row in one transaction or in a\n    negotiated set of interactions.\n\n    Interaction 2a: Creating and Activating the Conceptual Row\n\n    The management station must first determine the column\n    requirements, i.e., it must determine those columns for\n    which it must or must not provide values.  Depending on the\n    complexity of the table and the management station's\n    knowledge of the agent's capabilities, this determination\n    can be made locally by the management station.  Alternately,\n    the management station issues a management protocol get\n    operation to examine all columns in the conceptual row that\n    it wishes to create.  In response, for each column, there\n    are three possible outcomes:\n\n         - a value is returned, indicating that some other\n         management station has already created this conceptual\n         row.  We return to interaction 1.\n\n         - the exception `noSuchInstance' is returned,\n         indicating that the agent implements the object-type\n         associated with this column, and that this column in at\n         least one conceptual row would be accessible in the MIB\n         view used by the retrieval were it to exist. For those\n         columns to which the agent provides read-create access,\n         the `noSuchInstance' exception tells the management\n         station that it should supply a value for this column\n         when the conceptual row is to be created.\n\n         - the exception `noSuchObject' is returned, indicating\n         that the agent does not implement the object-type\n         associated with this column or that there is no\n         conceptual row for which this column would be\n         accessible in the MIB view used by the retrieval.  As\n         such, the management station can not issue any\n         management protocol set operations to create an\n         instance of this column.\n\n    Once the column requirements have been determined, a\n    management protocol set operation is accordingly issued.\n    This operation also sets the new instance of the status\n    column to `createAndGo'.\n\n    When the agent processes the set operation, it verifies that\n    it has sufficient information to make the conceptual row\n    available for use by the managed device.  The information\n    available to the agent is provided by two sources: the\n    management protocol set operation which creates the\n    conceptual row, and, implementation-specific defaults\n    supplied by the agent (note that an agent must provide\n    implementation-specific defaults for at least those objects\n    which it implements as read-only).  If there is sufficient\n    information available, then the conceptual row is created, a\n    `noError' response is returned, the status column is set to\n    `active', and no further interactions are necessary (i.e.,\n    interactions 3 and 4 are skipped).  If there is insufficient\n    information, then the conceptual row is not created, and the\n    set operation fails with an error of `inconsistentValue'.\n    On this error, the management station can issue a management\n    protocol retrieval operation to determine if this was\n    because it failed to specify a value for a required column,\n    or, because the selected instance of the status column\n    already existed.  In the latter case, we return to\n    interaction 1.  In the former case, the management station\n    can re-issue the set operation with the additional\n    information, or begin interaction 2 again using\n    `createAndWait' in order to negotiate creation of the\n    conceptual row.\n\n                             NOTE WELL\n\n         Regardless of the method used to determine the column\n         requirements, it is possible that the management\n         station might deem a column necessary when, in fact,\n         the agent will not allow that particular columnar\n         instance to be created or written.  In this case, the\n         management protocol set operation will fail with an\n         error such as `noCreation' or `notWritable'.  In this\n         case, the management station decides whether it needs\n         to be able to set a value for that particular columnar\n         instance.  If not, the management station re-issues the\n         management protocol set operation, but without setting\n         a value for that particular columnar instance;\n         otherwise, the management station aborts the row\n         creation algorithm.\n\n    Interaction 2b: Negotiating the Creation of the Conceptual\n    Row\n\n    The management station issues a management protocol set\n    operation which sets the desired instance of the status\n    column to `createAndWait'.  If the agent is unwilling to\n    process a request of this sort, the set operation fails with\n    an error of `wrongValue'.  (As a consequence, such an agent\n    must be prepared to accept a single management protocol set\n    operation, i.e., interaction 2a above, containing all of the\n    columns indicated by its column requirements.) Otherwise,\n    the conceptual row is created, a `noError' response is\n    returned, and the status column is immediately set to either\n    `notInService' or `notReady', depending on whether it has\n    sufficient information to (attempt to) make the conceptual\n    row available for use by the managed device.  If there is\n    sufficient information available, then the status column is\n    set to `notInService'; otherwise, if there is insufficient\n    information, then the status column is set to `notReady'.\n    Regardless, we proceed to interaction 3.\n\n    Interaction 3: Initializing non-defaulted Objects\n\n    The management station must now determine the column\n    requirements.  It issues a management protocol get operation\n    to examine all columns in the created conceptual row.  In\n    the response, for each column, there are three possible\n    outcomes:\n\n         - a value is returned, indicating that the agent\n         implements the object-type associated with this column\n         and had sufficient information to provide a value.  For\n         those columns to which the agent provides read-create\n         access (and for which the agent allows their values to\n         be changed after their creation), a value return tells\n         the management station that it may issue additional\n         management protocol set operations, if it desires, in\n         order to change the value associated with this column.\n\n         - the exception `noSuchInstance' is returned,\n         indicating that the agent implements the object-type\n         associated with this column, and that this column in at\n         least one conceptual row would be accessible in the MIB\n         view used by the retrieval were it to exist. However,\n         the agent does not have sufficient information to\n         provide a value, and until a value is provided, the\n         conceptual row may not be made available for use by the\n         managed device.  For those columns to which the agent\n         provides read-create access, the `noSuchInstance'\n         exception tells the management station that it must\n         issue additional management protocol set operations, in\n         order to provide a value associated with this column.\n\n         - the exception `noSuchObject' is returned, indicating\n         that the agent does not implement the object-type\n         associated with this column or that there is no\n         conceptual row for which this column would be\n         accessible in the MIB view used by the retrieval.  As\n         such, the management station can not issue any\n         management protocol set operations to create an\n         instance of this column.\n\n    If the value associated with the status column is\n    `notReady', then the management station must first deal with\n    all `noSuchInstance' columns, if any.  Having done so, the\n    value of the status column becomes `notInService', and we\n    proceed to interaction 4.\n\n    Interaction 4: Making the Conceptual Row Available\n\n    Once the management station is satisfied with the values\n    associated with the columns of the conceptual row, it issues\n    a management protocol set operation to set the status column\n    to `active'.  If the agent has sufficient information to\n    make the conceptual row available for use by the managed\n    device, the management protocol set operation succeeds (a\n    `noError' response is returned).  Otherwise, the management\n    protocol set operation fails with an error of\n    `inconsistentValue'.\n\n                             NOTE WELL\n\n         A conceptual row having a status column with value\n         `notInService' or `notReady' is unavailable to the\n         managed device.  As such, it is possible for the\n         managed device to create its own instances during the\n         time between the management protocol set operation\n         which sets the status column to `createAndWait' and the\n         management protocol set operation which sets the status\n         column to `active'.  In this case, when the management\n         protocol set operation is issued to set the status\n         column to `active', the values held in the agent\n         supersede those used by the managed device.\n\n    If the management station is prevented from setting the\n    status column to `active' (e.g., due to management station\n    or network failure) the conceptual row will be left in the\n    `notInService' or `notReady' state, consuming resources\n    indefinitely.  The agent must detect conceptual rows that\n    have been in either state for an abnormally long period of\n    time and remove them.  It is the responsibility of the\n    DESCRIPTION clause of the status column to indicate what an\n    abnormally long period of time would be.  This period of\n    time should be long enough to allow for human response time\n    (including `think time') between the creation of the\n    conceptual row and the setting of the status to `active'.\n    In the absence of such information in the DESCRIPTION\n    clause, it is suggested that this period be approximately 5\n    minutes in length.  This removal action applies not only to\n    newly-created rows, but also to previously active rows which\n    are set to, and left in, the notInService state for a\n    prolonged period exceeding that which is considered normal\n    for such a conceptual row.\n\n                     Conceptual Row Suspension\n\n    When a conceptual row is `active', the management station\n    may issue a management protocol set operation which sets the\n    instance of the status column to `notInService'.  If the\n    agent is unwilling to do so, the set operation fails with an\n    error of `wrongValue' or `inconsistentValue'.  Otherwise,\n    the conceptual row is taken out of service, and a `noError'\n    response is returned.  It is the responsibility of the\n    DESCRIPTION clause of the status column to indicate under\n    what circumstances the status column should be taken out of\n    service (e.g., in order for the value of some other column\n    of the same conceptual row to be modified).\n\n\n                      Conceptual Row Deletion\n\n    For deletion of conceptual rows, a management protocol set\n    operation is issued which sets the instance of the status\n    column to `destroy'.  This request may be made regardless of\n    the current value of the status column (e.g., it is possible\n    to delete conceptual rows which are either `notReady',\n    `notInService' or `active'.) If the operation succeeds, then\n    all instances associated with the conceptual row are\n    immediately removed."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class RowPointer(TextualConvention, ObjectIdentifier):
    description = 'Represents a pointer to a conceptual row.  The value is the\n         name of the instance of the first accessible columnar object\n         in the conceptual row.\n         For example, ifIndex.3 would point to the 3rd row in the\n         ifTable (note that if ifIndex were not-accessible, then\n         ifDescr.3 would be used instead).'
    status = 'current'

mibBuilder.exportSymbols("RADLAN-SNMPv2", TruthValue=TruthValue, RowPointer=RowPointer, RowStatus=RowStatus)
