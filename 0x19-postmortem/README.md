# README: The Great Typo Outage of 2024

## Introduction
Welcome to the documentation for the postmortem of "The Great Typo Outage of 2024." This file details the incident, its root cause, the resolution, and the measures taken to prevent future occurrences. This README is intended to provide a clear and humorous overview of the incident to help our team and future developers understand the importance of rigorous testing and code review.

## Issue Summary
- **Duration**: 1 hour and 20 minutes (10:00 - 11:20 EAT, June 8, 2024).
- **Impact**: Our beloved Holberton WordPress site greeted users with a `500 Internal Server Error`. Roughly 100% of the 2000 users who tried to access the site during this time were affected.
- **Root Cause**: A typo in the code, changing `class-wp-locale.php` to `class-wp-locale.phpp`.

## Debugging Process
1. **Initial Detection**: The issue was detected at 10:00 EAT when users reported `500 Internal Server Error` messages.
2. **Hero Arrives**: Brennan (BDB) began investigating the issue at 19:20 PST.
3. **Process Check**: Confirmed that Apache processes were running correctly using `ps aux`.
4. **Directory Investigation**: Confirmed the web server was serving content from `/var/www/html/`.
5. **Strace Attempt 1**: Ran `strace` on the `root` Apache process with no useful output.
6. **Strace Attempt 2**: Ran `strace` on the `www-data` process, revealing an `ENOENT` error for `class-wp-locale.phpp`.
7. **Code Review**: Identified the typo in `wp-settings.php`, line 137.
8. **Correction**: Removed the erroneous "p" from `class-wp-locale.phpp`, restoring it to `class-wp-locale.php`.
9. **Validation**: Successfully tested the fix with a `curl` command, receiving a `200 OK` response.
10. **Automation**: Wrote a Puppet manifest to automate fixing similar errors in the future.

## Root Cause and Resolution
- **Root Cause**: A typo in the `wp-settings.php` file caused WordPress to search for `class-wp-locale.phpp` instead of `class-wp-locale.php`.
- **Resolution**: The typo was corrected, and a Puppet manifest was created to automate the fix for any similar future occurrences.

## Preventative Measures
To prevent such incidents from happening again, we have implemented the following measures:
- **
- **Testing Protocols**: Develop and enforce rigorous testing procedures for all deployments.
- **Monitoring Setup**: Integrate uptime monitoring services like [UptimeRobot](https://uptimerobot.com/) to detect and alert on outages.
- **Automated Checks**: Create scripts to scan for common typos and errors in code.
- **Code Review Training**: Train the team on best practices for code reviews to minimize human errors.
- **Deploy Puppet Manifest**: Use the `0-strace_is_your_friend.pp` manifest to automate error fixes.

## Conclusion
The Great Typo Outage of 2024 was a reminder of the impact small errors can have on our systems. By implementing these measures, we aim to prevent similar issues and maintain a stable and reliable environment for our users.

Happy coding, and always double-check your "p"s! 🎉


## Contact
For further information or questions about this incident, 
please contact linetgitonga@gmail.com

## Puppet Manifest
The Puppet manifest created to automate the typo fix can be found [here](https://github.com/bdbaraban/holberton-system_engineering-devops/blob/master/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp).

## License
This documentation is licensed under the MIT License. See the LICENSE file for details.

ITS THE 'P' FOR ME 
