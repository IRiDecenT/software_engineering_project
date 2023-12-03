import request from '@/utils/request'


export const userRegister = (registerData) => {
    return request({
        method: 'POST',
        url: 'register/',
        headers: {
            'Content-Type': 'application/json'
        },
        data: registerData
    })
}

export const userLogin = (loginData) => {
    return request({
        method: 'POST',
        url: 'login/',
        headers: {
            'Content-Type': 'application/json'
        },
        data: loginData
    })
}

// 此处的uid是用户的id， 通过路由传递过来， js中用``定义模版字符串， ${}为占位符
export const getUserInfo = (uid) => {
    return request({
        method: 'GET',
        url: `getUserInfo/${uid}/`,
        headers: {
            'Content-Type': 'application/json'
        },
    })
}

export const getAlbums = (uid) => {
    return request({
        method: 'GET',
        url: `getAlbums/${uid}/`,
        headers: {
            'Content-Type': 'application/json'
        },
    })
}