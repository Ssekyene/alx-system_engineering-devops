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

|File						|Description							|
|-----------------------------------|-----------------------------------------------------|
|0-simply_match_school.rb		|A regular expression must match `School`			|
|1-repetition_token_0.rb		|A regular expression that will match repetting t's exactly from 2 to 5 times|


