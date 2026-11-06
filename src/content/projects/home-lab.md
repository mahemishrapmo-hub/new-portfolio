---
ref: PRJ-07
title: Home lab NAS on TrueNAS
status: in-progress
order: 7
featured: false
summary: A second-hand office tower turned into network storage on TrueNAS Community Edition, with every part bought used and checked before it went in.
tags: ['TrueNAS', 'Home lab', 'Infrastructure']
stack: ['TrueNAS Community Edition', 'ZFS']
data: Personal hardware. Nothing work related is stored on it.
updated: 2026-11-02
---

## The build

| Part | Choice |
| --- | --- |
| Chassis | HP 290 G1 microtower, Intel Core i5-7500, 8GB RAM |
| Boot drive | Micron 2300 256GB NVMe, bought used at 97 percent health |
| Storage | Two 4TB WD Red class drives |
| Operating system | TrueNAS Community Edition |

## Decisions

**Why this box.** It came as a pair with a small form factor desktop. The small form factor machine could not take two 3.5-inch drives, the tower could, so the tower got the job.

**Why TrueNAS Community Edition.** It is free, it is built on ZFS, and it does one thing well. Paying for a NAS operating system to run on a second-hand tower would defeat the point.

**Why used drives.** A used enterprise or NAS drive is good value if you read its SMART data before you trust it. Power-on hours, data written and health percentage go in a log before anything joins the pool. A drive with tens of thousands of hours on it is treated very differently from one with a few thousand.

## Next

Pool layout, snapshot schedule and the backup policy get written up here once the build is finished.
