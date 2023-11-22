import yaml

yml_str = '- type: META\n  count: 10\n  display_level: 1\n  tail_type: UPDATED_AT\n  base_version_id: 353790565\n  published: true\n  max_level: 2\n  last_updated_at: 2023-09-21T02:40:05.028Z\n  version_id: 353790658\n- type: DOC\n  title: Redis\n  uuid: KRrdRcQI3Ju8lwDl\n  url: izm4x6g46amupvwy\n  prev_uuid: ''\n  sibling_uuid: _MTrUbLS0Eqovsqw\n  child_uuid: ''\n  parent_uuid: ''\n  doc_id: 140525130\n  level: 0\n  id: 140525130\n  open_window: 1\n  visible: 0\n- type: DOC\n  title: Spring\n  uuid: _MTrUbLS0Eqovsqw\n  url: kmtx1uk1iaegn5dr\n  prev_uuid: KRrdRcQI3Ju8lwDl\n  sibling_uuid: q8eR_wETF01Mlfx_\n  child_uuid: FjAI4QAJI0Xisdhd\n  parent_uuid: ''\n  doc_id: 140414012\n  level: 0\n  id: 140414012\n  open_window: 1\n  visible: 0\n- type: DOC\n  title: AOP\n  uuid: FjAI4QAJI0Xisdhd\n  url: qb39fx0kk5aodeyh\n  prev_uuid: _MTrUbLS0Eqovsqw\n  sibling_uuid: 51iLtyZu9dE1uMZf\n  child_uuid: ''\n  parent_uuid: _MTrUbLS0Eqovsqw\n  doc_id: 140524198\n  level: 1\n  id: 140524198\n  open_window: 1\n  visible: 0\n- type: DOC\n  title: IoC\n  uuid: 51iLtyZu9dE1uMZf\n  url: qk4nheah7faf3pg4\n  prev_uuid: FjAI4QAJI0Xisdhd\n  sibling_uuid: ''\n  child_uuid: ''\n  parent_uuid: _MTrUbLS0Eqovsqw\n  doc_id: 140414070\n  level: 1\n  id: 140414070\n  open_window: 1\n  visible: 0\n- type: DOC\n  title: Java\n  uuid: q8eR_wETF01Mlfx_\n  url: ghgu8oa1152inwug\n  prev_uuid: _MTrUbLS0Eqovsqw\n  sibling_uuid: _x6z-_PFyGo545V2\n  child_uuid: PGtl6oylL3Vh46En\n  parent_uuid: ''\n  doc_id: 140411308\n  level: 0\n  id: 140411308\n  open_window: 1\n  visible: 0\n- type: DOC\n  title: JVM\n  uuid: PGtl6oylL3Vh46En\n  url: ofxv0sd4xs051gtf\n  prev_uuid: q8eR_wETF01Mlfx_\n  sibling_uuid: So5wE0Yf2CNwZzqj\n  child_uuid: ''\n  parent_uuid: q8eR_wETF01Mlfx_\n  doc_id: 140524421\n  level: 1\n  id: 140524421\n  open_window: 1\n  visible: 0\n- type: DOC\n  title: J.U.C\n  uuid: So5wE0Yf2CNwZzqj\n  url: cmpizc7kw4glyci6\n  prev_uuid: PGtl6oylL3Vh46En\n  sibling_uuid: ''\n  child_uuid: goCZqurev-k31EiD\n  parent_uuid: q8eR_wETF01Mlfx_\n  doc_id: 140412021\n  level: 1\n  id: 140412021\n  open_window: 1\n  visible: 0\n- type: DOC\n  title: Java线程池\n  uuid: goCZqurev-k31EiD\n  url: aen8z7aem2ry1vl2\n  prev_uuid: So5wE0Yf2CNwZzqj\n  sibling_uuid: ''\n  child_uuid: ''\n  parent_uuid: So5wE0Yf2CNwZzqj\n  doc_id: 140412079\n  level: 2\n  id: 140412079\n  open_window: 1\n  visible: 0\n- type: DOC\n  title: MySQL\n  uuid: _x6z-_PFyGo545V2\n  url: mad7h30ywkcciqeg\n  prev_uuid: q8eR_wETF01Mlfx_\n  sibling_uuid: ''\n  child_uuid: ZWg9gzPMohS8lt3V\n  parent_uuid: ''\n  doc_id: 140410699\n  level: 0\n  id: 140410699\n  open_window: 1\n  visible: 0\n- type: DOC\n  title: MySql索引\n  uuid: ZWg9gzPMohS8lt3V\n  url: hmi6nk4ebav8nrpm\n  prev_uuid: _x6z-_PFyGo545V2\n  sibling_uuid: ''\n  child_uuid: ''\n  parent_uuid: _x6z-_PFyGo545V2\n  doc_id: 140410767\n  level: 1\n  id: 140410767\n  open_window: 1\n  visible: 0\n'

result = yaml.load(yml_str, Loader=yaml.FullLoader)

print(result, type(result))

"""
[
  {
    "type":"META",
    "count":10,
    "display_level":1,
    "tail_type":"UPDATED_AT",
    "base_version_id":353790565,
    "published":true,
    "max_level":2,
    "last_updated_at":"datetime.datetime(, tzinfo=datetime.timezone.utc)",
    "version_id":353790658
  },
  {
    "type":"DOC",
    "title":"Spring",
    "uuid":"_MTrUbLS0Eqovsqw",
    "url":"kmtx1uk1iaegn5dr",
    "prev_uuid":"KRrdRcQI3Ju8lwDl",
    "sibling_uuid":"q8eR_wETF01Mlfx_",
    "child_uuid":"FjAI4QAJI0Xisdhd",
    "parent_uuid":"None",
    "doc_id":140414012,
    "level":0,
    "id":140414012,
    "open_window":1,
    "visible":0
  },
  {
    "type":"DOC",
    "title":"AOP",
    "uuid":"FjAI4QAJI0Xisdhd",
    "url":"qb39fx0kk5aodeyh",
    "prev_uuid":"_MTrUbLS0Eqovsqw",
    "sibling_uuid":"51iLtyZu9dE1uMZf",
    "child_uuid":"None",
    "parent_uuid":"_MTrUbLS0Eqovsqw",
    "doc_id":140524198,
    "level":1,
    "id":140524198,
    "open_window":1,
    "visible":0
  }
]
"""