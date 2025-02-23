# configuration specification for opensesame
#
# It is recommended to mount this file for development (then you get defaults+validation)
# simply run:
#
# kdb mount `pwd`/opensesame.spec spec:/sw/libelektra/opensesame/#0/current ni
# kdb spec-mount /sw/libelektra/opensesame/#0/current
#
# The second command needs to be re-executed when you change something in the spec.
#
# -_-
#  /

[]
mountpoint = opensesame.toml
infos/plugins = toml shell execute/set=reload-opensesame

[debug/backtrace]
description = tells to yield a backtrace on panic
example = full
default = 1
type = enum
check/enum = #_3
check/enum/#0 = 0
check/enum/#1 = 1
check/enum/#2 = full

[debug/ping/enable]
description = if periodic pings (keep-alive messages) should happen
type = boolean
default = 1

[debug/ping/timeout]
description = number of hours until ping again
type = unsigned_long
default = 24

[nextcloud/url]
description = URL to be used for sending messages.
required =

[nextcloud/chat]
description = which chat to use for sending messages.
required =
check/length/max = 8

[nextcloud/chat/licht]
description = which chat to use for sending licht messages.
required =
check/length/max = 8

[nextcloud/chat/ping]
description = which chat to use for sending ping messages. Note: this chat will be used even if debug/ping/enable=0.
required =
check/length/max = 8

[nextcloud/format/time]
description=Format to be used for formatting time within Nextcloud messages, e.g. when entry gets prohibited because of time. By default ISO 8601 (Hour-minute-second format). Example is locales time.
see/#0 = nextcloud/format/date
see/#1 = https://docs.rs/chrono/latest/chrono/format/strftime/index.html#specifiers
default = %T
example = %X

[nextcloud/format/datetime]
description=Format to be used for formatting dates within Nextcloud messages, e.g. in startup and ping. By default ISO 8601. Example is localized date and time.
see/#0 = nextcloud/format/time
see/#1 = https://docs.rs/chrono/latest/chrono/format/strftime/index.html#specifiers
default = %+
example = %c

[garage/enable]
description = enable garage HW (Endposition, further GPIO buttons)
type = boolean
default = 0

[pwr/enable]
description = enable PWR switch
type = boolean
default = 0

[bell/enable]
description = if hardware bell is connected
type = boolean
default = 0

[audio/bell]
description=audio file to play when bell is pressed. /dev/null means to not play anything.
default=/dev/null
check/path=
check/path/mode = r

[audio/alarm]
description=audio file to play on alarm. /dev/null means to not play anything.
default=/dev/null
check/path=
check/path/mode = r

[location/latitude]
description=Latitude for sunrise/sunset calculation. Default: Vienna
default=48.210033
type=double

[location/longitude]
description=Longitude for sunrise/sunset calculation. Default: Vienna
default=16.363449
type=double

[light/timeout]
description = time in seconds until lights go off by themselves
type = unsigned_long
default = 60

[watchdog/enable]
description=enables/disables watchdog
type = boolean
example = 1
default = 0

[environment/device]
description=Which device to use for the environment sensor. /dev/null means that no environment sensor is connected.
example = "/dev/i2c"
default = "/dev/null"

[environment/data/interval]
description=How often to get new data (default: every 60 seconds, which is the highest interval)
default = 6000
type = unsigned_short

