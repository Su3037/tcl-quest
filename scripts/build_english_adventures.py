"""English storyboards; code and observed values are shared between languages."""
import copy,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
A=json.loads((R/'site/adventures.json').read_text())
# setting, title, four (beat title, explanation) pairs, three input labels
E=[
('Morning Wake-up Station','Light up Chip with a greeting',[
('Await a command','Chip is asleep. puts sends the text after it to the output area, like a small loudspeaker.'),('Say hello','The first puts produces the first message. Double quotes keep the words together.'),('Get ready','The next puts runs after the first. Tcl executes these commands in order.'),('Hear the echo','Each puts normally starts a new line. Compare the speech bubbles with the output.')],['Mission input','A greeting in Chinese','Greet another friend']),
('Backpack Desk','A name is a label; a value is what it holds',[
('Name the pocket','set names a pocket and stores a value. The hero pocket holds a character name.'),('Store the coins','coins is the label. The number is the value stored inside that pocket.'),('Read the pockets','Inside double quotes, $hero and $coins read their stored values.'),('Read the backpack','Those values become part of a sentence, which puts displays.')],['Mission input','Bo with 8 coins','An empty wallet']),
('Three Bracket Doors','One message, three different journeys',[
('Prepare the message','Store a value in hero, then send a message through the three doors.'),('The quote door','Double quotes group a message and allow $hero to be replaced with its value.'),('The brace door','Braces preserve the text here. $hero is not substituted at this stage.'),('The bracket door','Square brackets run string toupper first, then give its result to puts.')],['Mission input','Use the name Bo','Use the name Cy']),
('Potion Bench','Multiply the ingredients, then add the bonus',[
('Set out ingredients','bottles records how many bottles there are; each records their individual energy.'),('Calculate the recipe','expr multiplies the inputs. Brackets give its result to set energy.'),('Add the bonus','incr adds a bonus to the current energy value and updates that pocket.'),('Finish the potion','puts $energy reads and displays the final total.')],['Mission input','2 × 5, plus 1','No bottles, but a bonus']),
('Launch Beacon','Connect three skills into one beam',[
('Connect the batteries','The beacon needs a name, a battery count and energy per battery.'),('Calculate energy','expr calculates the total, which is stored in energy.'),('Broadcast values','In double quotes, the variable names are replaced with the real name and energy.'),('Preserve a template','The final braces preserve the literal text $energy.')],['Mission input','Two batteries','Bo sets off']),
('Forest Coin Gate','A condition chooses the path',[
('Offer the coins','gate receives a coin count. Switch the input to see how the gatekeeper chooses.'),('Check the condition','Compare coins >= 10. Exactly 10 also satisfies “at least 10”.'),('Choose a branch','Use Enter when the condition is true and Wait otherwise. Only one branch runs.'),('Receive the answer','return passes the selected result back to the caller; puts displays it.')],['Mission input','8 coins: not enough','10 coins: just enough']),
('Item Shelf','A name with a space can still be one item',[
('Lay out the items','list records each item’s boundary. A multiword name must be grouped correctly.'),('Pack the backpack','An item name containing a space still occupies only one list slot.'),('Count the slots','llength counts elements rather than individual words.'),('Take the second item','lindex starts at 0, so index 1 selects the second item.')],['Mission input','Use a green pear','Add a compass']),
('Collection Trail','Let Chip collect each item in turn',[
('Start with an empty basket','Set total to 0 to give the running sum a starting point.'),('Collect the first item','foreach gives the first list element to n, then runs the loop body.'),('Keep collecting','Each incr total $n adds the current value to the existing sum instead of replacing it.'),('Finish the list','When no items remain, the loop finishes and puts displays total.')],['Mission input','Collect 1, 3 and 5','An empty list']),
('Sign Repair Shop','Turn messy text into a tidy sign',[
('Receive the old sign','clean receives raw text, including the spaces at its edges.'),('Clean the edges','The inner string trim removes edge whitespace. Spaces in the middle stay.'),('Make it uppercase','The outer string toupper converts the cleaned text to uppercase.'),('Hang the sign','return gives the new text back; puts displays it.')],['Mission input','A different sign','Keep a middle space']),
('Forest Supply Station','Help every friend who needs supplies',[
('Read the roster','Each row has a name and hunger value. Start with an empty selected list.'),('Visit each friend','foreach visits the records; lassign separates name and hunger.'),('Deliver supplies','Append a name only when hunger >= 5. Exactly 5 needs supplies too.'),('Write the receipt','Return the selected names as a list. Skipped friends do not appear in it.')],['Mission input','Everyone has eaten','Bo just qualifies']),
('Skill-card Bench','One recipe, many calls',[
('Define the skill','proc defines double. n is an argument waiting for a value at call time.'),('Supply an input','Calling double supplies its input for n. The next call can use another number.'),('Run the card','expr doubles n; return passes the computed result back.'),('Receive the result','puts displays the returned value. The procedure must not hard-code one answer.')],['Mission input','Input 3','Decimal input 2.5']),
('Character Archive','Find values by their attribute names',[
('Create a record','dict create stores attributes using keys such as name and hp.'),('Restore health','dict incr finds the hp key and increases its value.'),('Look up by name','dict get retrieves name and hp by key, without needing their positions.'),('Show the record','The two retrieved values form name:health, which puts displays.')],['Mission input','Restore only 5 points','Use Bo’s record']),
('Adventure Log Cabinet','Close after writing, reopen for reading',[
('Open for writing','open with w creates or overwrites a file. Its channel is stored in f.'),('Write two lines','puts $f writes to the file channel rather than the screen.'),('Close and reopen','close finishes writing. Reopen the same file with r to read it.'),('Read the log','Each gets reads one line; puts sends that line to the screen.')],['Mission input','A new diary page','Save Chinese text']),
('Safe Treasure Room','A zero divisor does not have to end the trip',[
('Supply two numbers','safeDivide receives a and b. Check for danger before calculating.'),('Check the divisor','When b is 0, return undefined immediately and skip the division.'),('Calculate safely','For a nonzero b, use double to perform floating-point division.'),('Continue the trip','Both calls return readable results. The zero-input branch protects this script.')],['Mission input','9 divided by 2','Divide a negative number']),
('Workshop Average Machine','Every ingredient counts',[
('Check the basket','Check llength first. An empty list returns 0 immediately.'),('Weigh the total','For a nonempty list, visit every number and accumulate total.'),('Share the ingredients','Divide the floating-point total by the element count to get the mean.'),('Deliver the tool','average should work for new lists, decimal values and empty input.')],['Mission input','Decimal values','An empty basket']),
('Chip City Tool District','Give your tool its own address',[
('Create a district','namespace eval lab creates a namespace to group related tools.'),('Add a tool','Define area inside lab, with width w and height h as its arguments.'),('Calculate the area','expr multiplies width and height. This is a teaching calculation, not an EDA engine.'),('Call the address','The full name lab::area tells Tcl which namespace contains the command.')],['Mission input','A 3 × 4 rectangle','Zero width']),
('Report Magnifier','Capture a number from one line of text',[
('Open the report','slackValue receives a whole line. Not every line will match the required format.'),('Find the pattern','regexp checks slack: followed by an optional minus sign, digits and optional decimal part.'),('Read the capture','When matched, value contains the number text. Otherwise the procedure returns NA.'),('Deliver the clue','The result is captured text, not a newly calculated timing value.')],['Mission input','Positive integer slack','A line that does not match']),
('Chip Blueprint Factory','A blueprint and an instance have different roles',[
('Draw a blueprint','oo::class defines Chip: a class used as the blueprint for objects.'),('Make an instance','Chip new creates an object. The constructor stores its input in that object’s name.'),('Call a method','Calling label on the object retrieves its own stored name.'),('Finish using it','destroy removes the object. Separate objects can keep separate names.')],['Mission input','Manufacture Wide','Manufacture Nano']),
('Teaching Flow Track','Send the parameters through three stations',[
('Receive configuration','mockFlow receives a design name and period. This lesson simulates text records only.'),('Check the period','For period <= 0, error reports failure instead of returning a normal flow.'),('Connect the stations','For a valid period, list groups the read, clock and report records.'),('Output the flow','This is a teaching checklist. No netlist is actually read and no timing is calculated.')],['Mission input','Wide with period 5','A zero period']),
('Timing Detective Desk','Follow the paths to the worst slack',[
('Receive the paths','Each record has a path name and slack. Empty input returns 0 and NA.'),('Inspect every path','Only slack < 0 is a violation. Zero is allowed. Visit every path.'),('Update the minimum','Start with the first actual record and keep the smaller slack; do not start at 0.'),('Close the case','Return violations and worst in a dictionary, then read both keys to print the report.')],['Mission input','All paths pass','An empty report'])]
assert len(E)==20
for s,(setting,title,beats,labels) in zip(A,E):
 s['setting']=setting;s['title']=title
 for step,(name,text) in zip(s['steps'],beats):step.update(title=name,text=text)
 for v,label in zip(s['variants'],labels):v['label']=label
(R/'site/adventures.en.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n')
print('Built 80 English story beats')
