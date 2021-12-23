from telegraph import Telegraph

tele_ = Telegraph()

def telegrapher(a_title: str, content: str) -> str:
    auth_name = tele_.create_account(short_name="@Mister_Dark_Prince")
    resp = tele_.create_page(
        title=a_title,
        author_name=auth_name,
        author_url="https://t.me/TGFRNDZ",
        html_content=content,
    )
    link_ = resp["url"]
    return link_


def int_list(list_):
    intlist = []
    for one in list_:
        if one.isdigit():
            one = int(one)
        intlist.append(one)
    return intlist

async def username_list(list_):
    u_list = []
    for one in list_:
        u_list.append((await bot.get_users(one)).username)
    return u_list
