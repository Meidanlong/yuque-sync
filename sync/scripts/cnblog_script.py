from datetime import datetime

from sync.domain.constant.contants import DATE_FORMAT
from sync.service.cnblog_service import get_cnblog_recent_post, delete_cnblog_post


def delete_posts_after_date(date_str: str):
    date = datetime.strptime(date_str, DATE_FORMAT)
    cnblog_map: dict[int, {}] = get_cnblog_recent_post()
    del_count = 0
    for cnblog in cnblog_map.values():
        date_created = cnblog['dateCreated']
        if date_created > date:
            post_id_ = cnblog['postid']
            success = delete_cnblog_post(post_id_)
            if success:
                print('deleted {title}'.format(title=cnblog['title']))
                del_count += 1
    return del_count


if __name__ == '__main__':
    date_str = '20231217T00:00:00'
    delete_posts_after_date(date_str)