def get_home_message():
    """
    ホーム画面で表示するメッセージの取得
    :return:
    """
    # todo 期間から該当するLTを取得し、参加表明済みか否かによってメッセージを変更する
    is_applied = False
    message = "次回のLT会は7/27(金)です"
    return {"message": message, "is_applied": is_applied}


def register_lt(title, time):
    print(f"{title}, {time}")
