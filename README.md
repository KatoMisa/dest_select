﻿# dest_select

## Overview

RTC for specifying destination using GUI

## Description



### Input and Output



### Algorithm etc



### Basic Information

|  |  |
----|---- 
| Module Name | dest_select |
| Description | RTC for specifying destination using GUI |
| Version | 1.0.0 |
| Vendor | rsdlab |
| Category | User Interface |
| Comp. Type | STATIC |
| Act. Type | PERIODIC |
| Kind | DataFlowComponent |
| MAX Inst. | 1 |

### Activity definition

<table>
  <tr>
    <td rowspan="4">on_initialize</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_finalize</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_startup</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_shutdown</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td rowspan="4">on_activated</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td rowspan="4">on_deactivated</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td rowspan="4">on_execute</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_aborting</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_error</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_reset</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_state_update</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_rate_changed</td>
    <td colspan="2"></td>
  </tr>
</table>

### InPorts definition

#### gui_in



<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedShortSeq</td>
    <td></td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>


### OutPorts definition

#### gui_out



<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedShort</td>
    <td></td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>

#### place



<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedWString</td>
    <td></td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>


### Service Port definition


### Configuration definition

#### place1




<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>Home</td>
    <td></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Widget</td>
    <td colspan="2">text</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### place2




<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>Reception desk</td>
    <td></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Widget</td>
    <td colspan="2">text</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### place3




<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>Room1</td>
    <td></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Widget</td>
    <td colspan="2">text</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### place4




<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>Room2</td>
    <td></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Widget</td>
    <td colspan="2">text</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>


## Demo

## Requirement

## Setup

### Windows

### Ubuntu

## Usage

## Running the tests

## LICENCE




## References




## Author


