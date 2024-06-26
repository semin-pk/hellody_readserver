from fastapi import APIRouter, HTTPException

from .fuc import check_Spotify_accesstoken, vodlist_spotify, vodlist_youtube, vodlist_watch, vodlist_rating, vodlist_spotify_firstuser, vodlist_popular

router = APIRouter(prefix='/home')

@router.get('/spotify/{user_id}')
async def magepage_spotify_list(user_id: int):
    try:
        if await check_Spotify_accesstoken(user_id):
            data = await vodlist_spotify(user_id)
            if data[0]['spotify'] != []:
                result = {
                    'status': True,
                    'response': data[0]['spotify']
                }
                return result
            else:
                data = await vodlist_spotify_firstuser(user_id)
                result = {
                    'status': True,
                    'response': data
                }
                return result
        else: 
            result = {
                'status': False
            }
            return result
    except:
        raise HTTPException(status_code=400, detail='error')

@router.get('/youtube/{user_id}')
async def magepage_youtude_list(user_id: int):
    try:
        data = await vodlist_youtube(user_id)
        return data
    except: 
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/watch/{user_id}')
async def magepage_watch_list(user_id: int):
    try:
        data = await vodlist_watch(user_id)
        return data[0]['vod_history']
    except: 
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/rating/{user_id}')
async def magepage_rating_list(user_id: int):
    try:
        data = await vodlist_rating(user_id)
        return data[0]['review_rating_based']
    except: 
        raise HTTPException(status_code=400, detail='error')
    
@router.get('/popular/{user_id}')
async def magepage_popular_list(user_id: int):
    try:
        data = await vodlist_popular(user_id)
        return data
    except: 
        raise HTTPException(status_code=400, detail='error')