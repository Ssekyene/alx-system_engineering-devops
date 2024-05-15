# 0x06. Regular expression
## Background Context
The focus of this project is to play with regular expressions(regex) using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

The used codes are similar to the Ruby code below with just replacing the regexp part, meaning the code in between the `//`:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

## Resources
* [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
* [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
* [Rubular is your best friend](https://rubular.com/)

|File						|Description							|
|-----------------------------------|-----------------------------------------------------|
|0-simply_match_school.rb		|A regular expression that will match `School`			|
|1-repetition_token_0.rb		|A regular expression that will match repetting `t's` exactly from 2 to 5 times|
|2-repetition_token_1.rb		|A regular expression that will match zero or one of `b`	|
|3-repetition_token_2.rb		|A regular expression that will match one or more of `t`	|
|4-repetition_token_3.rb		|A regular expression that will match zero or more of `t`	|
|5-beginning_and_end.rb			|A regular expression that will exactly match a string that starts with `h` ends with `n` and can have any single character in between|
|6-phone_number.rb			|A regular expression that will match a 10 digit phone number(simply 10 digits)	|
|7-OMG_WHY_ARE_YOU_SHOUTING.rb	|A regular expression that will only match capital letters	|

+ File: `100-textme.rb`
This script demonstrates how to run some statistics on the TextMe app text messages transactions.
##### Tasks:
+ Should output: `[SENDER],[RECEIVER],[FLAGS]`
	- The sender phone number or name (including country code if present)
	- The receiver phone number or name (including country code if present)
	- The receiver phone number or name (including country code if present)
##### Example:
```
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
+17272713208,+19172319348,-1:0:-1:0:-1
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
18572406905,14022180266,-1:0:-1:-1:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
12392190384,19148265919,-1:0:-1:-1:-1
$
```
