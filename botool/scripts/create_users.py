#!/usr/bin/env python
"""
Copyright 2013 Reed O'Brien <reed@reedobrien.com>.
All rights reserved. Use of this source code is governed by a
BSD-style license that can be found in the LICENSE file.


Purpose: Create groups, users, and roles from yaml config
"""
from __future__ import unicode_literals

import logging
import sys

import botocore.session

from btx import BTX

from botool.common import (
    parse_args,
    setup_arg_parser
)


def main():
    parser = setup_arg_parser()
    parser.add_argument("-u", "--users", action="store_true",
                        help="process users")
    parser.add_argument("-o", "--output-dir", type=str,
                        help="put creds for users here")
    parser.add_argument("-g", "--groups", action="store_true",
                        help="process users")
    parser.add_argument("-r", "--roles", action="store_true",
                        help="process users")
    parser.add_argument("-a", "--all", action="store_true",
                        help="Process users, groups, and roles")
    args = parse_args(parser)
    botox = BTX(args.f, debug=args.verbose, dryrun=args.dryrun,
                region=args.region)

    if args.roles:
        pass
        # if botox.config["roles"]:
        #     for role in botox.config["roles"]:
        #         botox("CreateRole", role_name=role["role_name"],
        #               assume_role_policy_document=role[
        #                   "assume_role_policy_document"])
        #         # botox("PutRolePolicy", **role)
        #         botox("PutRolePolicy", role_name=role["role_name"],
        #               policy_name=role["policy_name"],
        #               policy_document=role["policy_document"])

    if args.groups:
        pass
        # if botox.config["groups"]:
        #     for group in botox.config["groups"]:
        #         botox("CreateGroup", group_name=group["group_name"])
        #         botox("PutGroupPolicy", **group)

    if args.users:
        pass
        # if botox.config["users"]:
        #     for user in botox.config["users"]:
        #         user_name = user["user_name"]
        #         groups = user["groups"]
        #         if not botox("GetUser", user_name=user_name):
        #             botox("CreateUser", user_name=user_name)
        #         existing = botox("ListGroupsForUser", user_name=user_name).get("Groups", [])
        #         if groups:
        #             for group in groups:
        #                 if group not in existing:
        #                     botox("AddUserToGroup",
        #                           user_name=user_name,
        #                           group_name=group)
        #         for membership in existing:
        #             if membership["GroupName"] not in groups:
        #                 botox("RemoveUserFromGroup",
        #                       user_name=user_name,
        #                       group_name=membership["GroupName"])

if __name__ == "__main__":
    main()
