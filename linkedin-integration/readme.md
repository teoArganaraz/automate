# Linkedin Integration
This folder contains a series of examples of the use of Linkedin APIs in order to execute the following actions:

- Loggin with an account.
- Send a connection to an user.
- Verify connection status.
- Send message to an user.
- Check a conversation with an user.

## Official API

This documentation outlines the use of the [Python Client](https://github.com/linkedin-developers/linkedin-api-python-client), which serves as a wrapper for making requests to the LinkedIn API.

### Consumer API and Recent Updates

The provided examples exclusively rely on Consumer API products due to their more straightforward usage and fewer required permissions. It's important to note that other products on the LinkedIn platform demand additional permissions. The Consumer API, while having some limitations, allows basic functionalities like logging in, requesting basic profile information, and creating posts.

### Recent Changes and Challenges

Recently, the Consumer API underwent an update in August 2023, leading to the deprecation of the *r_lite_profile* scope and the */me* endpoint. This update brought about four scopes within the Consumer API:

- **openid**
- **profile**
- **email**
- **w_member_social**

However, the *profile* and *email* scopes lack specific endpoints, and the *openid* scope only offers the */userinfo* endpoint, which does not provide the essential URN (Uniform Resource Name) of the user. The URN serves as a crucial identifier for executing actions within the account.

### Incomplete Examples

The initial intention was to demonstrate the login process and create a post using the URN obtained through the */me* endpoint. However, due to the recent changes, these examples with the official API remain incomplete. To address this, we need to explore alternative approaches or await further updates from LinkedIn regarding accessing user identifiers and executing actions within the platform. Keep an eye on the official LinkedIn API documentation for the latest developments and guidance.


## Unofficial API

Trying to solve the problems with the official API we found an alternative with this [unofficial API](https://github.com/tomquirk/linkedin-api/tree/master).

This API allows us to execute most of the actions listed above only using a valid Linkedin account.

The example provided logs in with one user and sends a message to another user using the public ID.

The capabilities of this API can be extended to perform other tasks, such as specific searches on Linkedin or perform more actions.

