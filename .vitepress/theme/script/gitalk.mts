import Gitalk from 'gitalk';
import 'gitalk/dist/gitalk.css';

export default function createGitalk(path: string) {
    const clientID = process.env.OAUTH_CLIENT_ID as string;
    const clientSecret = process.env.OAUTH_CLIENT_SECRET as string;

    const gitalk = new Gitalk({
        clientID: clientID,
        clientSecret: clientSecret,
        repo: 'meidanlong.github.io',
        owner: 'Meidanlong',
        admin: ['Meidanlong'],
        id: path,      // 确保唯一性和长度小于 50
        distractionFreeMode: false  // 类似 facebook 的无干扰模式
    });
    gitalk.render('gitalk-container');
}