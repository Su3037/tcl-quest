#!/usr/bin/env python3
"""Authored English course. Executable code, outputs and grading rules stay identical."""
import copy,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
base=json.loads((ROOT/'site/curriculum.json').read_text())
# title, topic, story, explanations, task, hints, question, choices, diagram, pitfall, transfer
E=[
('Wake Up the Little Robot','puts · comments','The robot on Chip Island is asleep. Wake it with your first greeting.',
['puts tells Tcl to display some text. Think of it as a small loudspeaker: puts "Hello" says Hello. Double quotes keep the words of one message together.','A line beginning with # is a comment. It explains the code to people; Tcl does not run it. Start with one command per line.'],
'Print Hello, Tcl! and then Ready!, with each message on its own line.',
['Use two puts commands.','Wrap each message in double quotes.'],
'What happens to a line that begins with #?',['Tcl ignores it as a comment','It is printed','It is a variable'],['A puts command','Text goes to output','One message per line'],
'Use straight quotes ", not curly quotation marks. Tcl command names are case-sensitive.','Replace the greeting with your own name and run it again.'),
('Label Your Backpack','set · variable substitution','Before you set off, put your coins in a backpack pocket with a name.',
['A variable is a named pocket that holds a value. set coins 8 puts 8 in the pocket called coins. You can replace it with another value later.','Use $coins to read the value. In double quotes, Tcl replaces $hero and $coins with their stored values. set assigns a value; $ reads it.'],
'Create hero with the value Ada and coins with the value 12. Print Ada has 12 coins.',
['Use set hero Ada and set coins 12.','Use puts "$hero has $coins coins" to build the sentence.'],
'Which expression reads the value stored in coins?',['$coins','set $coins','"coins"'],['Label: coins','Store a value: 12','Read with $coins'],
'Do not put $ before the variable name when assigning it: use set coins 12.','Change the coin count, then print the same sentence again.'),
('The Three Bracket Doors','quotes · braces · brackets','Three doors treat the same message differently: substitute, preserve, or run a command first.',
['Double quotes group words and allow variable and command substitution. Braces group words while normally preserving their contents at this stage: {Hello $hero} keeps the dollar sign and name.','Square brackets run the command inside first and substitute its result. Tcl then passes that result to the surrounding command. Braces are also commonly used for scripts and expressions.'],
'Set hero to Ada. Print Hello Ada, then the literal text Hello $hero, then ADA on separate lines.',
['Use double quotes for the first line and braces for the second.','For the third line, use [string toupper $hero].'],
'Which form preserves the literal text $hero here?',['{Hello $hero}','"Hello $hero"','[Hello $hero]'],['" " allows substitution','{ } preserves the text','[ ] runs a command first'],
'Brackets run a Tcl command, not arbitrary text. Every opening bracket or brace needs its matching closing partner.','Change hero to Bo and predict all three lines before running them.'),
('Brew an Energy Potion','expr · incr · arithmetic','Let Tcl calculate the energy in your potion recipe.',
['expr evaluates arithmetic. set energy [expr {3 * 7}] calculates 21 and stores it. Braces around the expression let expr handle its variables safely and efficiently.','incr energy 4 adds 4 to an integer variable. Integer division drops the fractional part: 5 / 2 is 2, while 5 / 2.0 is 2.5.'],
'There are 3 bottles with 7 energy each and a bonus of 4. Store the total in energy and print 25.',
['Multiply the bottle count by the energy per bottle using expr.','Then use incr energy 4 and puts $energy.'],
'What does expr {5 / 2.0} return?',['2.5','2','5'],['3 bottles × 7','Add a bonus of 4','Total energy: 25'],
'incr expects an integer increment. Use expr when your calculation needs fractions.','Try a different bottle count and calculate the expected total yourself.'),
('BOSS · Repair the Launch Beacon','combined skills · variables and quoting','The launch beacon needs its name, energy and original template restored.',
['Combine the skills from the village: store values with set, calculate with expr and display with puts. Think about whether each output should contain a value or literal text.','Double quotes replace variables; braces preserve the literal template in this task. These three output lines deliberately use different rules.'],
'Set hero=Ada, cells=4 and each=5. Store their product in energy. Print Ada ready, Energy: 20, and the literal text $energy on three lines.',
['Use expr {$cells * $each} for the energy.','Use braces around $energy on the final output line.'],
'How can puts print the literal text $energy?',['puts {$energy}','puts "$energy"','puts $energy'],['Store the inputs','Calculate total energy','Broadcast values and a template'],
'The last line must preserve $energy; printing 20 again does not satisfy this part of the task.','Change the hero and battery count and predict which output lines will change.'),
('The Gatekeeper’s Choice','if · comparisons','The forest gate requires at least 10 coins. Help the gatekeeper make a choice.',
['if means “if this condition holds”. A true condition runs one script; else supplies the alternative. Numeric comparisons include >=, < and ==.','For text comparisons, prefer eq and ne: if {$name eq "Ada"}. Tcl if conditions and branch scripts are usually enclosed in braces. A procedure scaffold is provided here; you will study procedures in more detail later.'],
'Write gate {coins}. Return Enter for at least 10 coins and Wait otherwise. Print the result of gate 12.',
['Use if {$coins >= 10}.','Each branch should return its result: Enter or Wait.'],
'Which condition means “at least 10 coins”?',['$coins >= 10','$coins > 10','$coins < 10'],['Are coins ≥ 10?','Yes → Enter','No → Wait'],
'The boundary value 10 must be allowed. Compare numbers with ==; assign values with set.','Change the threshold to 20 and test 19, 20 and 21.'),
('Pack an Item List','list · lindex · llength · lappend','Pack a key, an apple and a map without losing each item’s boundary.',
['A list keeps track of its elements. list key "red apple" creates two elements, even though red apple contains a space. lappend adds another element to a list variable.','llength counts elements. lindex selects one by its index, starting at 0. The second item therefore has index 1.'],
'Create bag containing key, red apple and map in that order. Print the count 3 and then the second item, red apple.',
['Create the list with [list key "red apple" map].','Use llength for the count and lindex with index 1 for the second item.'],
'What is the index of the second element?',['1','2','0'],['A list preserves boundaries','3 items, including red apple','Index 1 selects the second item'],
'Do not treat every space as an element boundary. Use list and proper grouping when an item contains spaces.','Append a compass and verify that the list now contains four items.'),
('The Collecting Robot','foreach · for · while','The robot can repeat a job without asking you to copy the same command many times.',
['foreach takes each item from a list in turn and runs a script with that item. A running total starts at 0 and adds the current value on every turn.','for combines initialization, a condition and an update; while repeats while its condition is true. Make sure the condition can eventually become false. The task uses foreach.'],
'Visit 2, 4 and 6, accumulate their sum in total using foreach, and print 12.',
['Start with set total 0.','Inside foreach n {2 4 6}, use incr total $n.'],
'What does foreach do?',['Visits each list element in turn','Runs only the first element','Automatically sorts the list'],['Start total at 0','Add 2, then 4, then 6','Print total: 12'],
'Do not reset total inside the loop. That would discard the sum from previous turns.','Try {1 3 5}, then an empty list. Predict each total.'),
('Transform a Sign','string · trim · toupper · split/join','Clean a messy sign, convert the letters and hang up the new version.',
['string trim removes whitespace at the beginning and end of text. string toupper converts letters to uppercase. You can nest bracketed commands so that one result becomes another command’s input.','split turns text into a list using separator characters. join combines list elements with a chosen separator. They are useful for moving between structured data and readable text.'],
'Write clean {text} to trim both ends and convert to uppercase. Print the result for "  chip  ": CHIP.',
['Apply string trim to $text first.','Return [string toupper [string trim $text]].'],
'What does string trim remove?',['Whitespace at both ends','Every space in the text','All lowercase letters'],['Raw text with edge spaces','trim clears the edges','toupper makes it uppercase'],
'trim does not remove spaces in the middle of the text. Preserve those when cleaning a multiword sign.','Try "  chip island  " and check that the middle space remains.'),
('BOSS · Deliver Supplies','combined skills · filtering records','Three forest friends have different hunger levels. Find out who needs supplies.',
['Each record is a list containing a name and hunger value. foreach visits the records, and lassign extracts their fields into variables.','Use if to select records and lappend to collect their names. The returned value should remain a list so that names containing spaces keep their boundaries.'],
'Implement supply {rows}. Each row is {name hunger}. Return a list of names with hunger >=5. For the sample, print Ada Cy.',
['Check if {$hunger >= 5}.','Inside that branch, use lappend selected $name.'],
'Why do the checks use different character names?',['To verify that the rule works for new input','To make the code longer','Tcl only accepts three names'],['Read a {name hunger} record','Is hunger ≥ 5?','Append selected names'],
'Do not join the list before returning it; that can lose the boundaries of names containing spaces.','Raise the threshold to 8 and see which friends no longer need supplies.'),
('Make a Reusable Skill Card','proc · arguments · return','Put a greeting into a skill card that works for more than one name.',
['proc defines a reusable procedure, like a recipe with input slots. proc greet {name} {...} defines greet with an argument named name. Calling greet Ada supplies Ada for that argument.','Ordinary variables inside a procedure are usually local. return hands a result back to the caller; puts displays text. Arguments may also have default values.'],
'Implement double {n} to return twice its input. Print 14 for double 7.',
['Calculate with expr.','Use return [expr {$n * 2}] to pass the result back.'],
'Which command gives a computed result back to the caller?',['return','puts','#'],['Input n = 7','Call double','Return 14'],
'Printing inside a procedure does not usually provide the result that an outer expr needs.','Add times {n factor} so the multiplier becomes an argument too.'),
('Keep a Character Record','dict · array','Find an attribute by its name instead of remembering which numbered slot contains it.',
['A dictionary stores key/value pairs, such as hp mapped to 80 and name mapped to Ada. dict get reads a value, dict set changes it and dict exists checks whether a key is present.','Tcl also has arrays: set hero(hp) 80. An array is a collection of variable elements; a dictionary is a value that can be passed as an argument. This task practices dictionaries.'],
'Create a hero dictionary with name=Ada and hp=80. Increase hp by 20 and print Ada:100.',
['dict incr hero hp 20 updates the dictionary in variable hero.','dict get $hero hp reads the updated value.'],
'Which expression reads hp from the hero dictionary?',['dict get $hero hp','set hero(hp)','lindex hp hero'],['Dictionary: hero','name → Ada','hp → 100'],
'Reading a missing key raises an error. You can check with dict exists first.','Add a level key with the value 3.'),
('Save Your Adventure Log','open · puts · gets · close','Write your story to a file and read it back.',
['open returns a file channel, like a pipe connected to the file. Mode w creates or overwrites a file; r reads and a appends. puts $f writes text to that channel.','gets $f reads one line and close $f closes the channel. The browser uses an in-memory virtual filesystem; this does not automatically save a file on your computer. Each run starts a fresh environment.'],
'Write Level 13 and Saved as two lines in quest.txt. Close it, reopen for reading, and print both lines.',
['Write with puts $f "Level 13".','After closing the write channel, reopen using set f [open quest.txt r].'],
'What does mode w do to an existing file?',['Overwrites its contents','Only reads it','Automatically backs up every version'],['open quest.txt w','puts → file → close','open r → gets → close'],
'On a real computer, w overwrites an existing file. Practice with dedicated exercise filenames.','Use a to append a third line in local Tcl, then read the file again.'),
('Avoid an Error Trap','catch · error · error messages','A locked chest should not end the whole adventure. Learn how to handle failure.',
['catch runs a script and stores its result or error message in a variable. Completion code 0 means success; an ordinary error returns 1.','error reports an invalid situation explicitly. Errors are clues about your program. catch also handles completion codes such as return and break; this lesson concentrates on normal completion and ordinary errors.'],
'Implement safeDivide {a b}: return undefined when b is 0; otherwise use floating-point division. Print 2.5 for 5/2 and undefined for 5/0.',
['Check if {$b == 0} before dividing.','double($a) inside expr preserves fractions even with integer input.'],
'What does a catch result of 0 usually mean?',['The script completed normally','An ordinary error occurred','A file has size zero'],['Check the input','Valid → calculate','Invalid → explain why'],
'Safe division can validate its input before an error occurs; it does not have to wait for division to fail.','Try catch {error "Bad key"} msg and then print $msg.'),
('BOSS · Repair the Workshop','combined skills · general procedures','The workshop needs an average skill card that also handles an empty basket.',
['First add the values with foreach, then divide by the element count. An empty list has length 0; handle it before dividing.','Engineering scripts often calculate statistics. Use double to preserve fractional averages. The procedure accepts a single list argument, so group its values with braces at the call site.'],
'Implement average {numbers}. Return 0 for an empty list and the arithmetic mean otherwise. Print 5.0 for {2 4 9}.',
['Use llength to check for an empty list first.','After summing, return expr {double($total) / [llength $numbers]}.'],
'Why use double in the average calculation?',['To avoid losing fractions to integer division','To run the loop twice','To rename the variable'],['List → sum','Empty list returns 0 first','Sum ÷ count'],
'incr works with integers. Using expr for this sum also supports decimal inputs.','Try {1.5 2.5} and verify the result is 2.0.'),
('Enter Chip City','namespace · EDA commands','Take your everyday automation skills into a chip-design setting.',
['VLSI means very-large-scale integration; EDA software helps people design chips. Tcl often controls these tools, but the additional tool commands are not built into Tcl itself.','A namespace groups related commands and helps avoid name conflicts. Our lab::area is a teaching command that calculates a rectangle’s area; it does not perform real chip design.'],
'Inside namespace lab, implement area {w h} to return width times height. Print 42 for lab::area 6 7.',
['Define proc area inside namespace eval lab {...}.','Return [expr {$w * $h}].'],
'What does lab::area identify?',['A command named area in namespace lab','A video file','A built-in commercial EDA command'],['Namespace lab','Procedure area','lab::area 6 7 → 42'],
'EDA commands depend on the specific tool. They may not exist in an ordinary Tcl interpreter.','Create another namespace with its own area command and compare the full names.'),
('Find a Clue in a Report','regexp · captures','A report line contains a slack value. Extract the number.',
['regexp matches text against a regular-expression pattern. Parenthesized parts can capture a substring into a variable. A successful match returns 1; a failed match returns 0.','The pattern in this task allows an optional minus sign, integer digits and an optional decimal part. ^ and $ require the whole line to match. Return NA when the format does not match.'],
'Implement slackValue {line}. Accept the exact prefix slack: followed by an integer or decimal, optionally negative. Return the number text, or NA if it does not match. Print -0.25 for the sample.',
['Use a capturing group for the number.','A suitable pattern is {^slack: (-?[0-9]+(\\.[0-9]+)?)$}.'],
'What is a capture group used for?',['Saving the matched part of the text','Changing the report automatically','Adding two numbers'],['A report line','regexp matches the pattern','Capture number text or return NA'],
'This is a simplified teaching format. Real tool reports require patterns based on that tool’s documented format and units.','Try slack: 3, slack: -2.5 and a line without the slack prefix.'),
('Build a Chip Object','TclOO · class · constructor · method','Draw a blueprint, then manufacture objects from it.',
['A class is a blueprint; an object is a particular instance made from it. TclOO is included in Tcl 8.6+. A constructor initializes an object’s state, and methods operate on that object.','An object variable belongs to its instance. Two Chip objects can therefore keep different names. Call a method with $object method and destroy the object when you are finished.'],
'Create class Chip. Its constructor {value} stores name, and method label {} returns name. Create an object called Tiny and print Tiny.',
['label must return the object variable name.','Use return $name in the method.'],
'Which comparison best describes classes and objects?',['A blueprint and models made from it','A filename and its extension','Addition and multiplication'],['Class Chip','Object Tiny','Object Nova'],
'Call an object method using $object method, not object.method().','Add a rename {value} method that updates the object’s name.'),
('Build a Teaching Design Flow','source · modules · workflows','Separate configuration from operations so one script can serve different designs.',
['source reads and executes another Tcl file in the current interpreter. Loading changeable parameters from a configuration file is a common way to organize scripts.','Real EDA read, constraint, synthesis, place-and-route and report commands vary between tools. mockFlow only returns a teaching description; it calls no commercial tool and produces no GDS.'],
'Implement mockFlow {design period}. Raise an error for period <=0; otherwise return the list {read:design clock:period report:timing}. Print the flow for Tiny with period 10.',
['Use if {$period <= 0} {error "Period must be positive"}.','Use list instead of string concatenation to preserve a design name containing spaces.'],
'What does source config.tcl do?',['Executes that Tcl file','Turns it into a video','Automatically starts commercial EDA software'],['Configuration file','Load using source','Read → clock → report'],
'Here clock:10 is only text, not an EDA command that creates a real clock.','Try the design name My Chip and verify that llength still reports three steps.'),
('FINAL BOSS · Timing Report Detective','final project · statistics and validation','Chip City’s timing report has arrived. Count violating paths and find the worst slack.',
['The report is a list of {path slack} records. A slack below 0 counts as a violation; the smallest slack is the worst value. Return a dictionary so another script can use the results.','Handle empty input first. For nonempty input, initialize worst from the first actual record. Starting at 0 would incorrectly report 0 when all slack values are positive.'],
'Implement analyze {rows}, returning a dictionary with violations and worst. Empty input returns violations=0 and worst=NA. The sample prints Violations: 2 and Worst: -0.25 ns.',
['Return early for empty input. Otherwise initialize worst from the first record.','In foreach, test slack<0 and slack<worst separately, then return a dict create result.'],
'If every slack is positive, what should worst contain?',['The smallest positive value','Always 0','Always NA'],['A list of report records','Count slack < 0 · find minimum slack','Dictionary: violations / worst'],
'This is simplified teaching data. Real reports contain multiple checks and units; parse them according to the tool documentation.','Extend the project: read records from a text file, skip blank lines, reject invalid data and write CSV.')]
# Keep concept questions aligned with the Chinese version so quiz progress is shared.
Q={
1:('What do the double quotes in puts "Hello world" do?',['Group the sentence as one argument','Turn the text into a comment','Run the command twice']),
2:('Which command stores 12 in coins?',['set coins 12','set $coins 12','coins = 12']),
3:('What does puts {$hero} print?',['The literal text $hero','The value of hero','Nothing']),
4:('What is the result of expr {5 / 2}?',['2','2.5','An error']),
5:('Which approach makes a bug easier to find?',['Change one thing and run it','Change every line at once','Delete all the brackets']),
7:('What is the first index in a list?',['0','1','-1']),
8:('What is easy to forget in a while loop?',['Updating the state used by its condition','Writing PUTS in uppercase','Adding a website link']),
9:('Which command removes spaces at both ends of a string?',['string trim','string length','llength']),
16:('Is create_clock a built-in Tcl core command?',['No; it is usually provided by an EDA tool','Yes; every tclsh can run it','It is a browser command']),
17:('What does negative slack mean in this teaching setting?',['A timing requirement is not met','A file does not exist','The chip is already broken'])
}
assert len(E)==20
result=copy.deepcopy(base)
worlds=[('Starter Village','Make your code speak','Beacon Lighter'),('Logic Forest','Choose and repeat','Forest Guardian'),('Tool Workshop','Turn small skills into tools','Tool Maker'),('Chip City','Explore the VLSI setting','Timing Detective')]
for w,(name,sub,badge) in zip(result['worlds'],worlds):w.update(name=name,subtitle=sub,badge=badge,icon=['S','L','T','C'][result['worlds'].index(w)])
checks=[[],['The character name is stored in hero','coins stores the number 12'],[],['energy is 25'],['Energy is stored in the energy variable'],['Exactly 10 coins can enter','9 coins must wait','0 coins must wait'],['The list has three items','The final item is map'],['total stores the sum'],['Different text is cleaned','All spaces become an empty string'],['Empty input selects nobody','Boundary values and new names work'],['Handles zero','Handles negative inputs','Handles decimal inputs'],['The dictionary stores hp=100','The character name is preserved'],['The file was actually created'],['Negative values divide correctly','Other zero divisors are safe'],['Empty lists return 0','Fractional averages are preserved','Handles negative inputs'],['New dimensions work','Zero width has zero area'],['Recognizes positive integers','Recognizes decimals','Invalid lines return NA'],['A new object keeps its own name','Two objects keep separate names'],['A new design can produce a flow','Invalid periods are rejected','A multiword name still produces three steps'],['Empty reports have an explicit result','All-positive slack keeps a positive minimum','Zero slack is not a violation','Different names and ordering work']]
keys=['title','topic','story','explain','task','hints','quiz','choices','diagram','pitfall','transfer']
for l,english in zip(result['levels'],E):
 l.update(dict(zip(keys,english)))
 # Question order is authored independently; the correct choice is always first here.
 l['answer']=0
 if l['id'] in Q:l['quiz'],l['choices']=Q[l['id']]
 for key in ['starter','example']:
  l[key]=re.sub(r'(?m)^(\s*)#.*[\u3400-\u9fff].*$',lambda m:m[1]+('# TODO: complete the task described above.' if key=='starter' else '# A comment: Tcl does not execute this line.'),l[key])
 # Check labels are UI text, while the executable assertions remain unchanged.
 for i,c in enumerate(l['checks']):c['label']=checks[l['id']-1][i]
 d=ROOT/'lessons'/f'{l["id"]:02d}'
 text=f'# {l["id"]:02d} · {l["title"]}\n\n[中文](README.md) · [Course home](../../README.en.md)\n\n{l["story"]}\n\n'
 text+=f'![Lesson {l["id"]} scene](../../site/media/scenes/level-{l["id"]:02d}-en.svg)\n\n'
 text+='\n\n'.join(l['explain'])+'\n\n## Try this example\n\n```tcl\n'+l['example']+'\n```\n\n## Your mission\n\n'+l['task']+'\n\nExpected output:\n\n```text\n'+l['expected']+'\n```\n\n## Hints\n\n'+'\n\n'.join(l['hints'])+'\n\n## Watch out\n\n'+l['pitfall']+'\n\n## Think about it\n\n'+l['quiz']+'\n\n'+'\n'.join(f'{i+1}. {c}' for i,c in enumerate(l['choices']))+'\n\n<details><summary>Answer</summary>\n\n'+l['choices'][0]+'\n\n</details>\n\n## One more step\n\n'+l['transfer']+'\n'
 (d/'README.en.md').write_text(text)
(ROOT/'site/curriculum.en.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Built 20 English lessons')
